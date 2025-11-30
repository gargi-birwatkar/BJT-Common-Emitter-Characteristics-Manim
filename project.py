from manim import *
import sys
import random
#https://www.canva.com/design/DAGiGBl0XME/_iC9dHFo2CVgI4V6Et-nQw/edit?utm_content=DAGiGBl0XME&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton
class npntransistor(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.electron_list=[]
        self.p=23
        self.q=24
        self.r=25
        self.t=26
        self.u=27

    def construct(self):
        ''' grid = NumberPlane(
            x_range=[-7, 7, 1],  # X-axis from -7 to 7, step size 1
            y_range=[-4, 4, 1],  # Y-axis from -4 to 4, step size 1
            background_line_style={"stroke_color": TEAL, "stroke_width": 2, "stroke_opacity": 0.5}
         )
        self.add(grid)'''
        text3=Text("Bipolar Junction Transistor",font_size=50)
        

        self.play(FadeIn(text3))  # First, fade in at the center
        self.wait(2)
        self.play(FadeOut(text3)) 
        

        # Create N-type and P-type rectangles
        n_type = Rectangle(height=5, width=3, color=BLUE, fill_opacity=0.5).shift(LEFT*3)
        p_type = Rectangle(height=5, width=2, color=RED, fill_opacity=0.5)
        n_type2 = Rectangle(height=5, width=4, color=BLUE, fill_opacity=0.5).shift(RIGHT*3.5)

        # Animate their creation
        self.play(Create(n_type))
        self.wait(1)
        self.play(Create(p_type))
        self.wait(1)
        self.play(Create(n_type2))
        self.wait(1)

        # Labels for N-type and P-type materials
        label = VGroup(
            Text("N-type", font_size=34).next_to(n_type, DOWN),
            Text("P-type", font_size=34).next_to(p_type, DOWN),
            Text("N-type", font_size=34).next_to(n_type2, DOWN)
        )
        
        example = VGroup(
            MarkupText("Heavily Doped", font_size=24).next_to(n_type, UP),
            MarkupText("Lightly Doped", font_size=24).next_to(p_type, UP),
            MarkupText("Moderately Doped", font_size=24).next_to(n_type2, UP)            
        )

        # Animate text
        self.play(Write(label))
        self.play(Write(example))
        self.wait(2)
        
        dot1=Dot(radius=0.2,color=YELLOW).move_to(UP*3.5+LEFT*6.5)
        eletext=MarkupText(": Electron",font_size=30).move_to(UP*3.5+LEFT*5.5)

        dot2=Circle(radius=0.2,color=RED).move_to(UP*3+LEFT*6.5)
        holtext=MarkupText(": Holes",font_size=30).move_to(UP*3+LEFT*5.5)
        self.play(Create(dot1),Create(dot2),Write(holtext),Write(eletext))
        print("Afyter wait 2 vgroup")
        sys.stdout.flush()
        
        
# Given dot positions
        n_type_positions = [
          [-1.62145754, 2.32748337, 0.0],
[-1.64853099, -0.56571, 0.0],
[-1.66469697, -1.00599888, 0.0],
[-1.83738324, 1.16197685, 0.0],
[-2.17529617, 0.42056276, 0.0],
[-2.32218328, 2.26986922, 0.0],
[-2.16305124, -2.29110514, 0.0],
[-2.45508808, -2.13495575, 0.0],
[-2.56655543, -0.72681839, 0.0],
[-2.80904046, 1.24003731, 0.0],
[-2.85892655, 0.40631254, 0.0],
[-3.02649241, 0.03317784, 0.0],
[-3.06655434, -0.38320532, 0.0],
[-3.16028912, -2.18736817, 0.0],
[-3.46396808, -1.72513331, 0.0],
[-3.80784721, 1.55424255, 0.0],
[-3.80561187, -1.1754592, 0.0],
[-4.00693782, -1.40560399, 0.0],
[-4.18210706, 0.83875213, 0.0],
[-4.19300538, -1.71881904, 0.0]

        ]

        p_type_positions = [
          [-0.02770177, 0.77264254, 0.0],
[-0.02509315, -0.96051288, 0.0],
[-0.121872, 1.67542774, 0.0],
[-0.0880918, -1.67324036, 0.0],
[-0.15937237, -2.04494411, 0.0],
[-0.17941834, -0.25388167, 0.0],
[0.1323171, -1.37877965, 0.0],
[0.1628097, -0.69990232, 0.0],
[0.29326313, 1.90897672, 0.0],
[0.36457816, -0.20293228, 0.0],
[-0.2665519, 2.27138721, 0.0],
[-0.43316358, -1.68072631, 0.0]


        ]

        n_type2_positions = [
            
[2.36556611, -0.17339983, 0.0],
[1.6370259, -1.0247198, 0.0],
[2.31657719, -2.23645122, 0.0],
[2.57202, -2.3958087, 0.0],
[2.81214306, 1.52733532, 0.0],
[2.93422625, -2.37344917, 0.0],
[2.98252065, -0.33373557, 0.0],
[3.18391646, 1.93249981, 0.0],
[3.28746145, -0.54449876, 0.0],
[3.3676753, 0.4755289, 0.0],
[3.66051051, 1.70508472, 0.0],
[3.67646809, -1.96159982, 0.0],
[3.86684742, -1.31723152, 0.0],
[4.01894245, 0.53012901, 0.0],
[4.30279224, -0.05461015, 0.0],
[4.38870194, -1.46981623, 0.0],
[5.28700407, -0.02547089, 0.0],
[5.36283078, 2.22075411, 0.0]


        ]

        # Create and add dots at the specified locations
        n_type_dots = VGroup(*[Dot(point=np.array(pos), radius=0.12, color=YELLOW) for pos in n_type_positions])
        p_type_dots = VGroup(*[Circle(radius=0.12, color=RED).move_to(np.array(pos)) for pos in p_type_positions])
        n_type2_dots = VGroup(*[Dot(point=np.array(pos), radius=0.12, color=YELLOW ) for pos in n_type2_positions])
       
        self.add(n_type_dots, p_type_dots, n_type2_dots)
        self.wait(2)

        elee = VGroup(*n_type2_dots, *n_type_dots, *p_type_dots)
        #self.add(elee)
      
        n_type_dots = VGroup(*n_type_dots)
        p_type_dots = VGroup(*p_type_dots)
        n_type2_dots = VGroup(*n_type2_dots)

        n_type_group = VGroup(n_type, n_type_dots)
        p_type_group = VGroup(p_type, p_type_dots)
        n_type2_group = VGroup(n_type2, n_type2_dots)

        # Group all transistor parts
        transistor = VGroup(n_type, p_type, n_type2,elee)
        self.wait(1)
        # Step 1: Move N-type parts closer to P-type
        self.play(
            n_type_group.animate.shift(RIGHT * 0.5),
            n_type2_group.animate.shift(LEFT * 0.5),
            run_time=2
            )
        self.wait(1)
        rect1 = Rectangle(
            width=1.2, height=5, 
            color=WHITE,  # Outline color
            fill_color=WHITE,  # Fill color
            fill_opacity=0.2  # Adjust transparency (0 = fully transparent, 1 = fully opaque)
        ).move_to(LEFT*1)

        rect2 = Rectangle(
            width=1.2, height=5, 
            color=WHITE,  # Outline color
            fill_color=WHITE,  # Fill color
            fill_opacity=0.2  # Adjust transparency (0 = fully transparent, 1 = fully opaque)
        ).move_to(RIGHT*1)

        
        for i in range(6):
            
            self.play(AnimationGroup(
    # Move the dots to their positions
    n_type_dots[i].animate.move_to((p_type.get_left()[0] + 0.15, n_type.get_top()[1] - 0.45 - 0.75 * i, 0)),
    n_type_dots[i+6].animate.move_to((p_type.get_left()[0] + 0.45, p_type.get_top()[1] - 0.45 - 0.75 * i, 0)),
    n_type2_dots[i].animate.move_to((p_type.get_right()[0] - 0.15, p_type.get_top()[1] - 0.45 - 0.75 * i, 0)),
    n_type2_dots[i+6].animate.move_to((p_type.get_right()[0] - 0.45, p_type.get_top()[1] - 0.45 - 0.75 * i, 0)),
    p_type_dots[i].animate.move_to(np.array([n_type.get_right()[0] - 0.45, n_type.get_top()[1] - (0.45 + 0.75 * i), 0])),
    p_type_dots[i+6].animate.move_to(np.array([n_type2.get_left()[0] + 0.45, n_type2.get_top()[1] - (0.45 + 0.75 * i), 0])),
    lag_ratio=0.1  # Smooth sequential movement
))

# Transform each dot into a circle with a '+' sign immediately after moving
            self.play(AnimationGroup(
    Transform(n_type_dots[i], VGroup(Circle(radius=0.15, color=YELLOW).move_to(n_type_dots[i].get_center()), Text('-', font_size=24).move_to(n_type_dots[i].get_center()))),
    Transform(n_type_dots[i+6], VGroup(Circle(radius=0.15, color=YELLOW).move_to(n_type_dots[i+6].get_center()), Text('-', font_size=24).move_to(n_type_dots[i+6].get_center()))),
    Transform(n_type2_dots[i], VGroup(Circle(radius=0.15, color=YELLOW).move_to(n_type2_dots[i].get_center()), Text('-', font_size=24).move_to(n_type2_dots[i].get_center()))),
    Transform(n_type2_dots[i+6], VGroup(Circle(radius=0.15, color=YELLOW).move_to(n_type2_dots[i+6].get_center()), Text('-', font_size=24).move_to(n_type2_dots[i+6].get_center()))),
    Transform(p_type_dots[i], VGroup(Circle(radius=0.15, color=YELLOW).move_to(p_type_dots[i].get_center()), Text('+', font_size=24).move_to(p_type_dots[i].get_center()))),
    Transform(p_type_dots[i+6], VGroup(Circle(radius=0.15, color=YELLOW).move_to(p_type_dots[i+6].get_center()), Text('+', font_size=24).move_to(p_type_dots[i+6].get_center()))),
    lag_ratio=0.1  # Ensures sequential transformation
))
           
        self.play(Create(rect1),Create(rect2))
        # Step 2: Fade out labels before rotation
        self.play(FadeOut(example),run_time=1)
        Texs=MarkupText("Depletion\n Region",font_size=30).shift(UP*3)
        self.play(Write(Texs))
        self.wait(2)
        self.play(FadeOut(label),FadeOut(Texs),FadeOut(rect1),FadeOut(rect2))
        # Step 3: Rotate the transistor 90 degrees smoothly
        self.play(Rotate(transistor, angle=PI/2), run_time=2)
        self.play(transistor.animate.move_to(ORIGIN))
        self.wait(1)
        self.play(transistor.animate.scale(0.4), run_time=1)
        self.wait(2)
        
        transistor = VGroup(n_type, p_type, n_type2)
        self.play(FadeOut(elee),FadeOut(dot1),FadeOut(dot2),FadeOut(holtext),FadeOut(eletext))

        textt=Text("CONSTRUCTION",font_size=40).move_to([-4,3,0])
    

        self.play(Write(textt))
        example2= VGroup(
            Text("Heavily Doped", font_size=19).move_to(n_type.get_center()),
            Text("Lightly Doped", font_size=19).move_to(p_type.get_center()),
            Text("Moderately\n \tDoped", font_size=19).move_to(n_type2.get_center())            
        )
        # Step 4: Adjust labels **AFTER rotation**
        self.play(Write(example2))
        self.wait(2)

        
         # Step 5: Add Arrows and Labels for Emitter, Base, and Collector
        emitter_arrow = Arrow(start=n_type.get_bottom(), end=n_type.get_bottom() + DOWN * 1.5, buff=0.1, color=WHITE)
        emitter_label = Text("Emitter(N-type)", font_size=28).next_to(emitter_arrow, DOWN, buff=0.2)

        base_arrow = Arrow(start=p_type.get_center()+LEFT*1, end=p_type.get_center() + LEFT * 2.5, buff=0.2, color=WHITE)
        base_label = Text("Base(P-type)", font_size=28).next_to(base_arrow, LEFT, buff=0.2)

        collector_arrow = Arrow(start=n_type2.get_top(), end=n_type2.get_top() + UP * 1.5, buff=0.1, color=WHITE)
        collector_label = Text("Collector(N-type)", font_size=28).next_to(collector_arrow, UP, buff=0.2)
        
        # Animate Arrows and Labels
        self.play(Create(emitter_arrow), Write(emitter_label))
        self.play(Create(base_arrow), Write(base_label))
        self.play(Create(collector_arrow), Write(collector_label))
        # Optional: Scale down the transistor
        
        self.wait(2)
        arrowss=VGroup(emitter_arrow,collector_arrow,base_arrow)
        arrows_name=VGroup(emitter_label,base_label,collector_label)


        self.play(FadeOut(example2),FadeOut(arrowss),FadeOut(arrows_name),FadeOut(transistor),FadeOut(textt))



        #circuit
        text2=Text("CIRCUIT",font_size=50).scale(0.8).move_to([-5,3,0])
    

        self.play(Write(text2)) # First, fade in at the center
        
        self.wait(2)

        self.play(FadeIn(transistor))
       # Complete Circuit Lines
        circuit_lines = VGroup(
            # Emitter to Ground
            Line(start=n_type.get_center() + DOWN * 0.65, end=DOWN * 3.2, color=WHITE),
            Line(start=LEFT*0.6+DOWN*3.2,end=DOWN*3.2+RIGHT*0.6,color=WHITE),
            Line(start=LEFT*0.4+DOWN*3.4,end=DOWN*3.4+RIGHT*0.4,color=WHITE),
            Line(start=LEFT*0.2+DOWN*3.6,end=DOWN*3.6+RIGHT*0.2,color=WHITE),


            # Collector UP SMALL
            Line(start=UP*1.8, end=UP * 3, color=WHITE),

            # Base to Input Signal through Resistor
            Line(start=p_type.get_center() + LEFT * 1, end=p_type.get_center() + LEFT * 5, color=WHITE),
            Line(start=p_type.get_center() + LEFT * 5, end=DOWN * 1+LEFT*5, color=WHITE),
            Line(start=DOWN * 1.15+LEFT*5, end=DOWN * 3+LEFT*5, color=WHITE),


            # Connect Collector to Vcc (Resistor in Between) TO GROUND
            Line(start=UP * 3, end=RIGHT * 3 + UP * 3, color=WHITE),
            Line(start=RIGHT * 3 + UP * 3, end=RIGHT * 3, color=WHITE),
             Line(start=RIGHT * 3 + DOWN * 0.3, end=RIGHT * 3 + DOWN * 3, color=WHITE),


            #  Ground
            Line(start=DOWN * 3+LEFT*5, end=RIGHT * 3 + DOWN * 3, color=WHITE),

            #battery
            #VCC voltage
            Line(RIGHT*2.2, RIGHT*3.7, color=WHITE),  
            Line(RIGHT*2.5+DOWN*0.1, RIGHT*3.25+DOWN*0.1, color=WHITE),
            Line(RIGHT*2.2+DOWN*0.2, RIGHT*3.7+DOWN*0.2, color=WHITE),  
            Line(RIGHT*2.5+DOWN*0.3, RIGHT*3.25+DOWN*0.3, color=WHITE),
            #BASE VOLTAGE
            Line(LEFT*5.5+DOWN*1,LEFT*4.5+DOWN*1, color=WHITE),  # 
            Line(LEFT*5.3+DOWN*1.15,LEFT*4.8+DOWN*1.15, color=WHITE),


            #BASE VOLTAGE NAMES
            MarkupText("+",font_size=30).shift(LEFT * 5.3+DOWN*0.7),
            MarkupText("-",font_size=30).shift(LEFT * 5.3+DOWN*1.5),
            MarkupText("V<sub>BB</sub>",font_size=30).shift(LEFT*6+DOWN*1),

             #COLLECTOR VOLTAGE NAMES
            MarkupText("+",font_size=30).shift(RIGHT*3.3+UP*0.4),
            MarkupText("-",font_size=30).shift(RIGHT*3.3+DOWN*0.5),
             MarkupText("V<sub>CC</sub>",font_size=30).shift(RIGHT*4.5+DOWN*0.2)

            
        )
        
        self.play(Create(circuit_lines))
        emitter_label.set_font_size(18).move_to(n_type.get_center())
        base_label.set_font_size(18).move_to(p_type.get_center())
        collector_label.set_font_size(18).move_to(n_type2.get_center())

        self.play(Write(emitter_label))
        self.play(Write(base_label))
        self.play(Write(collector_label))

        forward=Text("Forward \n   Bias",font_size=28).move_to(LEFT*3+DOWN*1)
        reverse=Text("Reverse Bias",font_size=28).rotate(PI/2).move_to(RIGHT*2)
        self.play(FadeIn(forward),FadeIn(reverse))
       

        ib = Triangle(color=WHITE, fill_opacity=1).scale(0.2).rotate(-PI/2).move_to(p_type.get_center() + LEFT * 2)
        ie= Triangle(color=WHITE, fill_opacity=1).scale(0.2).rotate(PI).move_to(DOWN * 2.5)
        ic = Triangle(color=WHITE, fill_opacity=1).scale(0.2).rotate(PI/2).move_to(UP*3+RIGHT*1.5)
        ib_label = MarkupText("I<sub>B</sub>", font_size=28).move_to(LEFT*2.5)
        ic_label = MarkupText("I<sub>C</sub>", font_size=28).move_to(UP*2.5+RIGHT*1.5)
        ie_label = MarkupText("I<sub>E</sub>", font_size=28).move_to(DOWN*2.5+RIGHT*0.4)
        self.play(Write(ib_label),Write(ic_label),Write(ie_label))
        display=VGroup(forward,reverse)
        # Display the triangle
        self.play(Create(ib),Create(ic),Create(ie))

        self.wait(5)

        self.play(FadeOut(arrows_name),FadeOut(display))
        


##WORKING
        text1=Text("WORKING",font_size=48).move_to(text2.get_center())
        

        self.play(TransformMatchingShapes(text2, text1))
        
        on=Text("WHEN KEY IS CLOSED!",font_size=20).move_to(UP*1.2+LEFT*3)
        self.play(Write(on))
        self.wait(4)
        #self.play(FadeOut(on))
 # Create and position a single electron at the left side of the N-type region
    

        dot2.set_color(YELLOW).move_to(UP*2.5+LEFT*6)
        dot1.move_to(UP*2+LEFT*6)
        holtext.move_to(UP*2.5+LEFT*5)

        
        eletext.move_to(UP*2+LEFT*5)
        
        self.play(Create(dot2),Write(holtext),Create(dot1),Write(eletext))


        for i in range(1,5):
             for j in range(1,8):
                 electrons = Dot(radius=0.1, color=YELLOW).move_to([(n_type.get_left()[0] + 0.25*j), (n_type.get_bottom()[1] + 0.25*i), 0])
                 self.electron_list.append(electrons)

# Convert list to VGroup for animation
        electronss = VGroup(*self.electron_list)
        
        
# CReate holes
        hole1= Circle(radius=0.1, color=YELLOW).move_to([p_type.get_left()[0] + 0.25, p_type.get_bottom()[1] + 0.25, 0])
        hole2= Circle(radius=0.1, color=YELLOW).move_to([p_type.get_left()[0] + 0.75, p_type.get_bottom()[1] + 0.25, 0])
        self.play(Create(hole1),Create(hole2),Create(electronss),run_time=0.5)

# Manage the movement of a single electron to base
        # Function to create a looping path animation
        def electron_cycle(electron, path_points, run_time=4):
            path = VMobject()
            print("hii gargi-----------------------",path_points)
            sys.stdout.flush();
            path.set_points_as_corners(path_points)
            return MoveAlongPath(electron, path, run_time=run_time)
       
       
        electron_path = [
                    [p_type.get_left()[0] + 0.25, p_type.get_bottom()[1] + 0.25, 0],
                    p_type.get_center() + LEFT * 1,  # Start near Base
                    p_type.get_center() +LEFT * 5,  # Move left
                    p_type.get_center() +LEFT * 5 + DOWN * 3,  # Move down
                    LEFT * 5 + DOWN * 3,
                    DOWN * 2.8,
                    #DOWN * 0.8,
                    [n_type.get_left()[0] + 0.25, n_type.get_bottom()[1] + 0.25, 0]  # Move to end
                    ]

        electron_path3 = [
                    [-0.25 ,-0.8 , 0]  ,
                    p_type.get_center() + LEFT * 0.1,  # Start near Base  # Move down
                    UP*3,
                    UP*3+RIGHT*3,
                    RIGHT*3+DOWN*3,
                    DOWN*3+ORIGIN,
                    (n_type.get_left()[0] + 0.75, n_type.get_bottom()[1] + 0.25, 0)  # Move to end
                    ]
        electron_path4 = [
            [-4.4408921e-16, -8.0000000e-01 , 0.0000000e+00],
                    ORIGIN,  # Start near Base  # Move down
                    UP*3,
                    UP*3+RIGHT*3,
                    RIGHT*3+DOWN*3,
                    DOWN*3+ORIGIN,
                    (0, n_type.get_bottom()[1] + 0.25, 0)  # Move to end
                    ]
        electron_path5 = [
                    [0.25 ,-0.8 ,0],
                    p_type.get_center() + RIGHT * 0.1,  # Start near Base  # Move down
                    UP*3,
                    UP*3+RIGHT*3,
                    RIGHT*3+DOWN*3,
                    DOWN*3+ORIGIN,
                    (n_type.get_right()[0] - 0.75, n_type.get_bottom()[1] + 0.25, 0)  # Move to end
                    ]
        electron_path6 = [
                    [0.5, -0.8,0],
                    p_type.get_center() + RIGHT * 0.25,  # Start near Base  # Move down
                    UP*3,
                    UP*3+RIGHT*3,
                    RIGHT*3+DOWN*3,
                    DOWN*3+ORIGIN,
                    (n_type.get_right()[0] - 0.5, n_type.get_bottom()[1] + 0.25, 0)  # Move to end
                    ]
        electron_path7 = [
            [0.75 ,-0.8   ,0],
                    p_type.get_center() + RIGHT * 0.75,  # Start near Base  # Move down
                    UP*3,
                    UP*3+RIGHT*3,
                    RIGHT*3+DOWN*3,
                    DOWN*3+ORIGIN,
                    (n_type.get_right()[0] - 0.25, n_type.get_bottom()[1] + 0.25, 0)  # Move to end
                    ]       
        electron_path1 = [
            [p_type.get_left()[0] + 0.75, p_type.get_bottom()[1] + 0.25, 0],
                    p_type.get_center() + LEFT * 0.25,  # Start near Base
                    p_type.get_center() +LEFT * 5,  # Move left
                    p_type.get_center() +LEFT * 5 + DOWN * 3,  # Move down
                    LEFT * 5 + DOWN * 3,
                    DOWN * 2.8,
                    DOWN * 0.8,
                    (n_type.get_left()[0] + 0.5, n_type.get_bottom()[1] + 0.25, 0)  # Move to end
                    ]

        self.n=28
        self.m=29
        
        electron_cycle1=[23,16,9,2]
        electron_cycle2=[24,17,10,3]
        electron_cycle3=[25,18,11,4]
        electron_cycle4=[26,19,12,5]
        electron_cycle5=[27,20,13,6]
        def move_electrons(cycle, start_electron, path,runtime):
            if start_electron in electron_cycle1:
                if self.p>0:
                    self.p=start_electron-7
                else:
                    self.p=23
            elif start_electron in electron_cycle2:
                if self.q>0:
                    self.q=start_electron-7
                else:
                    self.q=24
            elif start_electron in electron_cycle3:
                if self.r>0:
                    self.r=start_electron-7
                else:
                    self.r=25
            elif start_electron in electron_cycle4:
                if self.t>0:
                    self.t=start_electron-7
                else:
                    self.t=26
            elif start_electron in electron_cycle5:
                
                if self.u>0:
                    self.u=start_electron-7
                else:
                    self.u=27
            ele_path=VMobject()
            ele_path.set_points_as_corners(path)
            
            pos21=self.electron_list[start_electron].get_center()
            
            index=cycle.index(start_electron)
            s111 = cycle[(index + 1) % len(cycle)]
            pos112=self.electron_list[s111].get_center()
            s122 = cycle[(index + 2) % len(cycle)]
            pos211=self.electron_list[s122].get_center()
            s133= cycle[(index +3) % len(cycle)]
                    
                  
            print("hi-----------in move electrons ",path)
            sys.stdout.flush()
            return AnimationGroup(self.electron_list[s111].animate.move_to(pos21),self.electron_list[s122].animate.move_to(pos112),self.electron_list[s133].animate.move_to(pos211),MoveAlongPath(self.electron_list[start_electron],ele_path,run_time=runtime)  ) 
                



        for _ in range(4):
                    
                     # Call function

# Call function with predefined electron cycles and paths
                    
                    if(self.n>0 ):
                        self.n=self.n-7
                    else:
                        self.n=21
                    single_electron = self.electron_list[self.n] 
                    pos=single_electron.get_center()
                    print("n is ",self.n)
                    sys.stdout.flush()

                   
                    # Define the cycle order
                    cycle_order = [21, 14, 7, 0]  # This order repeats continuously
                    s_index = cycle_order.index(self.n)  # Find the current index of `n` in the cycle

    # Loop through the 3 next values in the cycle
                      # Always take the next three values
                    s = cycle_order[(s_index + 1) % len(cycle_order)]  # Wrap around with modulo
                    pos11 = self.electron_list[s].get_center()
                    s11 = cycle_order[(s_index + 2) % len(cycle_order)]  # Wrap around with modulo
                    pos22 = self.electron_list[s11].get_center()

                    s22 = cycle_order[(s_index + 3) % len(cycle_order)]  # Wrap around with modulo
                    print("Next n:", self.n)  # Debugging output
                    sys.stdout.flush()
                    

                    if(self.m>1):
                        self.m= self.m-7
                    else:
                        self.m=22
                    single_electron1 = self.electron_list[self.m] 
                     # Select electron
                    pos1=single_electron1.get_center()
                    print("m is ",self.m)
                   
        # Looping movement
                  
                    # Define the cycle order
                    cycle_order = [22, 15, 8, 1]

# Get index of the current m value in the cycle
                    index = cycle_order.index(self.m)

# Loop through the next three values in the cycle
                     
                    s2 = cycle_order[(index + 1) % len(cycle_order)]  # Get next value in cycle
                    pos2 = self.electron_list[s2].get_center()  # Get position

                    s3 = cycle_order[(index + 2) % len(cycle_order)]  # Get next value in cycle
                    pos3 = self.electron_list[s3].get_center()  # Get position

                    s4 = cycle_order[(index + 3) % len(cycle_order)]  # Get next value in cycle
                    # Get position
                     # Move animation
    
                  

                    print("Next n:", self.m)  # Debugging output
                    sys.stdout.flush()
                    self.play(single_electron.animate.move_to([p_type.get_left()[0] + 0.25, p_type.get_bottom()[1] + 0.25, 0]), FadeOut(hole1),single_electron1.animate.move_to([p_type.get_left()[0] + 0.75, p_type.get_bottom()[1] + 0.25, 0]),
        FadeOut(hole2),run_time=3)
                    self.play(
    AnimationGroup(
        electron_cycle(single_electron, electron_path),
        FadeIn(hole1),
        electron_cycle(single_electron1, electron_path1),
        FadeIn(hole2),run_time=6),AnimationGroup(
        
        self.electron_list[s2].animate.move_to(pos1),
        self.electron_list[s3].animate.move_to(pos2),
        self.electron_list[s4].animate.move_to(pos3),
        self.electron_list[s].animate.move_to(pos),
        self.electron_list[s11].animate.move_to(pos11),
        self.electron_list[s22].animate.move_to(pos22),
        lag_ratio=0  # Ensures everything runs in parallel
    ),move_electrons(electron_cycle1,self.p,electron_path3,5),move_electrons(electron_cycle2,self.q,electron_path4,6),move_electrons(electron_cycle3,self.r,electron_path5,7),
    move_electrons(electron_cycle4,self.t,electron_path6,8),
    move_electrons(electron_cycle5,self.u,electron_path7,9)
)


        self.wait(2)
            
       