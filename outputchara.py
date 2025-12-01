from manim import *
import numpy as np

class BJTExperimentalGraph(Scene):
    def construct(self):
        # Set up axes
        axes = Axes(
            x_range=[0, 8, 1],
            y_range=[-0.5, 7, 1],
            x_length=8,
            y_length=6,
            axis_config={"color": WHITE}
        ).shift(LEFT*2 +DOWN*0.5)

        # Create labels first (unpositioned)
        x_label = MarkupText("V<sub>CE</sub> (V)", font_size=24)
        y_label = MarkupText("I<sub>C</sub> (mA)", font_size=24).rotate(90*DEGREES)
        title = MarkupText("BJT Output Characteristics for CE Configuration", font_size=32)

        # Data with explicit knee points at V_CE=0.7V
        data = {
            0:[
    (0, 0),
    (0.5, 0.5),
    (1, 0.6),
    (2, 0.65),
    (3, 0.7),
    (4, 0.75),
    (5, 0.8),
    (6, 0.8),
    (7, 0.85),
    (8, 0.9),
    
],
            10: [(0.0, 0.0), (0.2, 0.5), (0.7, 1.5), (1.0, 1.8), (2.0, 2.0), (5.0, 2.1), (8.0, 2.2)],
            20: [(0.0, 0.0), (0.2, 1.0), (0.7, 2.8), (1.0, 3.5), (2.0, 3.9), (5.0, 4.0), (8.0, 4.1)],
            30: [(0.0, 0.0), (0.2, 1.5), (0.7, 4.0), (1.0, 5.2), (2.0, 5.8), (5.0, 6.0), (8.0, 6.1)]
        }
        line_dash=[(0,0),(2.0, 2.0),(2.0, 3.9),(2.0, 5.8)]
        colors = [GRAY, BLUE, YELLOW,PINK]
        curves = VGroup()
        knee_dots = VGroup()  # To mark transition points

        for i, (ib, points) in enumerate(data.items()):
             # Skip cutoff for main curves
            
            # Create curve
            curve = axes.plot_line_graph(
                x_values=[x for x,y in points],
                y_values=[y for x,y in points],
                line_color=colors[i],
                stroke_width=4
            )
            
            
            # Label
            label = MarkupText(f"I<sub>B</sub>={ib}μA", font_size=24, color=colors[i])
            label.next_to(curve["line_graph"].points[-1], UL, buff=0.1)
            
            curves.add(curve["line_graph"], label)
          

       

        # Region labels
        saturation_label =Text("Saturation Region", font_size=24).next_to(axes.c2p(4, 3), UP*5)
        
        cutoff_label = Text("Cutoff Region", font_size=24).next_to(axes.c2p(5,0),UP)
        
        active_label = Text("Active Region", font_size=24).move_to(UP*2.5+LEFT*4.5)

        # ANIMATION SEQUENCE
        # 1. Create axes
        self.play(Create(axes), run_time=1.5)
        
        # 2. Animate labels moving into place
        self.play(
            title.animate.to_edge(UP),
            x_label.animate.next_to(axes.x_axis, DOWN, buff=0.3),
            y_label.animate.next_to(axes.y_axis, LEFT, buff=0.3),
            run_time=1
        )
        
        # 3. Draw curves and knee points
        self.play(LaggedStart(*[Create(c) for c in curves], lag_ratio=3), run_time=8)
        
       
        
       
        points = [(0,0),(2.0, 2.0),(2.0, 3.9),(2.0, 5.8),(2.0,7.4)]
        #[(0, 0), (1.0, 1.8), (1.0, 3.5), (1.0, 5.2),(1.0, 7.2)]
        graph_points = [axes.c2p(x, y) for x, y in points]

        # 3. Create a SOLID line first
        solid_line = VMobject(stroke_color=RED, stroke_width=2.5)
        solid_line.set_points_as_corners(graph_points)

        # 4. Convert to dashed line (works in all Manim versions)
        dashed_line = DashedVMobject(
            solid_line,
            num_dashes=25,  # Adjust density of dashes
            color=RED
        )

        # 5. Add dots at points (optional)
        dots = VGroup(*[Dot(p, color=RED, radius=0.06) for p in graph_points])

        # 6. Animate
       
        self.play(
            Create(dashed_line),
            LaggedStart(*[FadeIn(dot) for dot in dots], lag_ratio=0.2),
            run_time=2
        )
        self.wait(2)
       # 4. Add divider through knee points
        self.play(
           
            Write(saturation_label),
            Write(active_label),
             Write(cutoff_label),
            run_time=3
        )
        self.wait(2)
        # Create a background rectangle for the note
        note_rect = RoundedRectangle(
            height=2, 
            width=4,
            corner_radius=0.2,
            fill_color=WHITE,
            fill_opacity=0.9,
            stroke_color=BLUE,
            stroke_width=2
        ).to_edge(UP*2+RIGHT, buff=0.5)
        # Create the note content with proper formatting
        note_title = Text("Saturation Region", font_size=28, color=BLUE_D)
        note_content = VGroup(
           
            Paragraph(
                "- Low V_CE",
                "- Both junctions forward biased",
                "- I_C reaches maximum",
                "- Acts as closed switch",
                font_size=18,
                color=BLACK,
               
                line_spacing=0.4
            )
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        # Position the note elements
        note_title.next_to(note_rect.get_top(), DOWN, buff=0.3)
        note_content.next_to(note_title.get_top(), DOWN, buff=0.5)
       

        # Group everything together
        note_group = VGroup(note_rect,note_title,note_content)

        # Animation
        self.play(FadeIn(note_group, shift=DOWN+LEFT))
        self.wait(3)
        
        note_rect2 = RoundedRectangle(
            height=2, 
            width=4,
            corner_radius=0.2,
            fill_color=GREEN,
            fill_opacity=0.8,
            stroke_color=BLUE,
            stroke_width=2
        ).to_edge(DOWN*5.5+RIGHT, buff=0.5)

        # Create the note content with proper formatting
        note_title2 = Text("Active Region", font_size=28, color=BLACK)
        note_content2 = VGroup(
           
            Paragraph(
                "- Flat I_C vs V_CE curve",
                "- Base-emitter forward biased",
                "- Base-collector reverse biased",
                "- I_C ≈ β·I_B",
                font_size=18,
                color=BLACK,
               
                line_spacing=0.4
            )
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        # Position the note elements
        note_title2.next_to(note_rect2.get_top(), DOWN, buff=0.3)
        note_content2.next_to(note_title2.get_top(), DOWN, buff=0.5)
         # Add left padding

        # Group everything together
        note_group2 = VGroup(note_rect2, note_title2, note_content2)

        # Animation
        self.play(FadeIn(note_group2, shift=RIGHT))
        self.wait(3)
        
        # Create a background rectangle for the note
        note_rect3 = RoundedRectangle(
            height=2, 
            width=4,
            corner_radius=0.2,
            fill_color=PURPLE,
            fill_opacity=0.9,
            stroke_color=BLUE,
            stroke_width=2
        ).to_corner(DOWN+RIGHT, buff=0.5)

        # Create the note content with proper formatting
        note_title3 = Text("Cutoff Region", font_size=28, color=WHITE)
        note_content3 = VGroup(
            Paragraph(
                "- I_B = 0 operation",
                "- Both junctions reverse biased",
                "- I_C ≈ 0 (transistor OFF)",
                font_size=18,
                color=WHITE,
               
                line_spacing=0.4
            )
        )

        # Position the note elements
        note_title3.next_to(note_rect3.get_top(), DOWN, buff=0.3)
        note_content3.next_to(note_title3.get_top(), DOWN, buff=0.5)
   

        # Group everything together
        note_group3 = VGroup(note_rect3, note_title3, note_content3)

        # Animation
        self.play(FadeIn(note_group3, shift=LEFT+UP))
        self.wait(3)
        
                    
            