from manim import *
import numpy as np

class BJTExperimentalGraph(Scene):
    def construct(self):
        # Set up axes
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[-0.5, 7, 1],
            x_length=8,
            y_length=6,
            axis_config={"color": WHITE}
        ).shift(DOWN*0.5)

        # Create labels first (unpositioned)
        x_label = MarkupText("V_CE (V)", font_size=24)
        y_label = MarkupText("I_C (mA)", font_size=24).rotate(90*DEGREES)
        title = MarkupText("BJT Output Characteristics", font_size=32)

        # Data with explicit knee points at V_CE=0.7V
        data = {
            0:  [(x, 0) for x in np.linspace(0, 10, 5)],
            10: [(0.0, 0.0), (0.2, 0.5), (0.7, 1.5), (1.0, 1.8), (2.0, 2.0), (5.0, 2.1), (10.0, 2.2)],
            20: [(0.0, 0.0), (0.2, 1.0), (0.7, 2.8), (1.0, 3.5), (2.0, 3.9), (5.0, 4.0), (10.0, 4.1)],
            30: [(0.0, 0.0), (0.2, 1.5), (0.7, 4.0), (1.0, 5.2), (2.0, 5.8), (5.0, 6.0), (10.0, 6.1)]
        }
        line_dash=[(0,0),(2.0, 2.0),(2.0, 3.9),(2.0, 5.8)]
        colors = [GRAY, BLUE, GREEN, YELLOW]
        curves = VGroup()
        knee_dots = VGroup()  # To mark transition points

        for i, (ib, points) in enumerate(data.items()):
            if ib == 0: continue  # Skip cutoff for main curves
            
            # Create curve
            curve = axes.plot_line_graph(
                x_values=[x for x,y in points],
                y_values=[y for x,y in points],
                line_color=colors[i],
                stroke_width=4
            )
            
            
            # Label
            label = MarkupText(f"Ib={ib}μA", font_size=24, color=colors[i])
            label.next_to(curve["line_graph"].points[-1], UR, buff=0.1)
            
            curves.add(curve["line_graph"], label)
          

        # DIVIDER LINE - passes through all knee points
        divider = DashedLine(
            start=axes.c2p(0.7, -0.5),
            end=axes.c2p(0.7, 7),
            color=RED,
            stroke_width=2.5,
            dash_length=2.15
        )

        # Region labels
        saturation_label = MarkupText("Saturation_Region", font_size=24).next_to(axes.c2p(4, 3), UP+RIGHT*10)
        
        cutoff_label = MarkupText("Cutoff_Region", font_size=24).next_to(axes.c2p(0,0), UP+RIGHT*5)
        
        active_label = MarkupText("Active_Region", font_size=24).move_to(UP*3+LEFT*3.5)

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
        self.play(LaggedStart(*[Create(c) for c in curves], lag_ratio=0.3), run_time=3)
        
        # 4. Add divider through knee points
        self.play(
           
            Write(saturation_label),
            Write(active_label),
             Write(cutoff_label),
            run_time=1.5
        )
        
       
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
        
        