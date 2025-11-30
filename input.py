from manim import *
import sys
import math
import time  #
class BJTInputCharacteristics(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.electron_list=[]
        self.p=23
        self.q=24
        self.r=25
        self.t=26
        self.u=27
        self.m=29
        self.n=28
    def vibrate_dot(self,dot, dt):
            dot.set_y(dot.base_y + 0.05 * math.sin(2 * math.pi * time.time() * 2))
    def construct(self):
        ''' grid = NumberPlane(
            x_range=[-7, 7, 1],  # X-axis from -7 to 7, step size 1
            y_range=[-4, 4, 1],  # Y-axis from -4 to 4, step size 1
            background_line_style={"stroke_color": TEAL, "stroke_width": 2, "stroke_opacity": 0.5}
         )
        self.add(grid)'''
        

        
        n_type = Rectangle(height=5, width=3, color=BLUE, fill_opacity=0.5).shift(LEFT*3)
        p_type = Rectangle(height=5, width=2, color=RED, fill_opacity=0.5)
        n_type2 = Rectangle(height=5, width=4, color=BLUE, fill_opacity=0.5).shift(RIGHT*3.5)
        self.play(Create(n_type))
        self.wait(1)
        self.play(Create(p_type))
        self.wait(1)
        self.play(Create(n_type2))
        self.wait(1)
        self.play(
            n_type.animate.shift(RIGHT * 0.5),
            n_type2.animate.shift(LEFT * 0.5),
            run_time=2
            )
        self.wait(1)
        transistor = VGroup(n_type, p_type, n_type2)
        self.play(Rotate(transistor, angle=PI/2), run_time=2)
        self.play(transistor.animate.move_to(ORIGIN))
        self.wait(1)
        self.play(transistor.animate.scale(0.4), run_time=1)
        self.wait(2)
        
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
        ib = Triangle(color=WHITE, fill_opacity=1).scale(0.2).rotate(-PI/2).move_to(p_type.get_center() + LEFT * 2)
        ie= Triangle(color=WHITE, fill_opacity=1).scale(0.2).rotate(PI).move_to(DOWN * 2.5)
        ic = Triangle(color=WHITE, fill_opacity=1).scale(0.2).rotate(PI/2).move_to(UP*3+RIGHT*1.5)
        ib_label = MarkupText("I<sub>B</sub>", font_size=28).move_to(LEFT*2.5)
        ic_label = MarkupText("I<sub>C</sub>", font_size=28).move_to(UP*2.5+RIGHT*1.5)
        ie_label = MarkupText("I<sub>E</sub>", font_size=28).move_to(DOWN*2.5+RIGHT*0.4)
        self.play(Write(ib_label),Write(ic_label),Write(ie_label))
        
        # Display the triangle
        self.play(Create(ib),Create(ic),Create(ie))

        
        self.play(Create(circuit_lines))
        
        dot1=Dot(radius=0.2,color=YELLOW).move_to(UP*2+LEFT*6.5)
        eletext=MarkupText(": Electron",font_size=30).move_to(UP*2+LEFT*4.5)

        dot2=Circle(radius=0.2,color=RED).move_to(UP*3+LEFT*6.5)
        dot2.set_color(YELLOW).move_to(UP*2.5+LEFT*6)
        dot1.move_to(UP*2+LEFT*6)
        holtext=MarkupText(": Holes",font_size=30).move_to(UP*2.5+LEFT*5)
        self.play(Create(dot1),Create(dot2),Write(holtext),Write(eletext))
        

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
            if start_electron not in cycle: return AnimationGroup()
            index=cycle.index(start_electron)
            s111 = cycle[(index + 1) % len(cycle)]
            pos112=self.electron_list[s111].get_center()
            s122 = cycle[(index + 2) % len(cycle)]
            pos211=self.electron_list[s122].get_center()
            s133= cycle[(index +3) % len(cycle)]
                    
                  
            
         
            return AnimationGroup(self.electron_list[s111].animate.move_to(pos21),self.electron_list[s122].animate.move_to(pos112),self.electron_list[s133].animate.move_to(pos211),MoveAlongPath(self.electron_list[start_electron],ele_path,run_time=runtime)  ) 
                
       
        volt_control=Circle(radius=1,fill_color=RED, fill_opacity=0.6).move_to(RIGHT*5.5+DOWN*2)
        label1=Text(f"Volts", font_size=24)
            # <- Puts text in center
        label1.move_to(volt_control.get_center()) 
        self.volt_control11=VGroup(hole1,hole2,volt_control,label1)
        self.play(Create(volt_control), Write(label1)) 
        for volt in range(0,10,4):
           
            print("the 24 center is: ",self.electron_list[24].get_center())
            print("the 25 center is: ",self.electron_list[25].get_center())
            print("the 27 center is: ",self.electron_list[27].get_center())
            self.play(FadeOut(label1))
            label1=Text(f"{volt} Volts", font_size=24)
            label1.move_to(volt_control.get_center()) 
            self.play(Write(label1)) 
            # <- Puts text in center
           
           
            if(volt==4):
             for _ in range(2):
                for i in range(0,28):
                    if i in[21,14,7,1,22,15,8,0,23,24,17,16,10,9,2,3]:
                        self.electron_list[i].clear_updaters()
                                 
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
                s = cycle_order[(s_index + 1) % len(cycle_order)] 
                print("the position of s is :",(s_index + 1) % len(cycle_order))# Wrap around with modulo
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
                    
               
                print(type(self.electron_list[0]))
                
               
                self.play(single_electron.animate.move_to([p_type.get_left()[0] + 0.25, p_type.get_bottom()[1] + 0.25, 0]), FadeOut(hole1),single_electron1.animate.move_to([p_type.get_left()[0] + 0.75, p_type.get_bottom()[1] + 0.25, 0]),
                FadeOut(hole2),run_time=3)
                
                self.play(self.electron_list[s2].animate.move_to(pos1),
                                self.electron_list[s3].animate.move_to(pos2),
                                self.electron_list[s4].animate.move_to(pos3),
                                self.electron_list[s].animate.move_to(pos),
                                self.electron_list[s11].animate.move_to(pos11),
                                self.electron_list[s22].animate.move_to(pos22),
                                lag_ratio=0  # Ensures everything runs in parallel
                                )
                self.play(AnimationGroup(
                electron_cycle(single_electron, electron_path),
                FadeIn(hole1),
                electron_cycle(single_electron1, electron_path1),
                FadeIn(hole2),run_time=6),move_electrons(electron_cycle1,self.p,electron_path3,5),move_electrons(electron_cycle2,self.q,electron_path4,6))
                
                
            elif(volt==0 or volt==2):
                for electron in self.electron_list:
                            electron.base_y = electron.get_y()
                            electron.add_updater(self.vibrate_dot)
                self.wait(2)
                
                                
            else:
                for electron in self.electron_list:
                        electron.clear_updaters()  
                      
                              
                for _ in range(2):
                    
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
                    
                    self.play(self.electron_list[s2].animate.move_to(pos1),
                                    self.electron_list[s3].animate.move_to(pos2),
                                    self.electron_list[s4].animate.move_to(pos3),
                                    self.electron_list[s].animate.move_to(pos),
                                    self.electron_list[s11].animate.move_to(pos11),
                                    self.electron_list[s22].animate.move_to(pos22),
                                    lag_ratio=0  # Ensures everything runs in parallel
                                    )
                        
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
                                move_electrons(electron_cycle5,self.u,electron_path7,9))
                    self.wait(2)
                    
                    
        self.play(FadeOut(label1))
        self.play(FadeOut(transistor),FadeOut(circuit_lines),FadeOut(electronss),FadeOut(holtext),FadeOut(dot1),FadeOut(dot2),FadeOut(eletext),FadeOut(ib),FadeOut(ib_label),FadeOut(ic),FadeOut(ic_label),FadeOut(ie),FadeOut(ie_label),FadeOut(self.volt_control11))              
                            
        

       
        # Axes
        axes = Axes(
            x_range=[0, 1.1, 0.1],  # Extended x_range slightly for clarity
            y_range=[0, 220, 20],   # I_B range
            axis_config={"color": WHITE},
            x_length=7,
            y_length=5,
        ).add_coordinates()

        # Labels
        x_label = axes.get_x_axis_label(MarkupText("V<sub>BE</sub>"))
        y_label = axes.get_y_axis_label("I_B (\mu A)")
        title = Text("BJT Input Characteristics (CE Configuration)").scale(0.6).to_edge(UP)

        # Data points
        data = {
            "V<sub>CE</sub> = 2V": [
                (0, 0), (0.50, 0), (0.58, 4.5), (0.66, 17.9), (0.74, 46.3), 
                (0.82, 88.9), (0.90, 152.6), (1.00, 200)
            ],
            "V<sub>CE</sub>= 5V": [
                (0, 0), (0.52, 0), (0.60, 4.5), (0.70, 13.5), (0.78, 34.2), 
                (0.86, 68.9), (0.94, 123.2), (1.05, 180)
            ],
            "V<sub>CE</sub> = 10V": [
                (0, 0), (0.54, 0), (0.62, 3.6), (0.72, 10.9), (0.80, 29.2), 
                (0.88, 60.8), (0.96, 112.6), (1.05, 160)
            ]
        }

        colors = [RED, GREEN, BLUE]
        graphs = []
        labels = []

        for i, (label, points) in enumerate(data.items()):
            graph = axes.plot_line_graph(
                x_values=[p[0] for p in points],
                y_values=[p[1] for p in points],
                line_color=colors[i],
                vertex_dot_radius=0.05
            )
            graphs.append(graph)

            # Position label near the last point, slightly above to avoid overlap
            last_x, last_y = points[-1]
            label_mob = MarkupText(label, color=colors[i]).scale(0.5)
            label_mob.next_to(axes.c2p(last_x, last_y), UP * (0.5 + i * 0.4)+RIGHT*1)  # Offset each label upwards
            
            labels.append(label_mob)

        # Display all elements
        self.play(Write(title))
        self.play(Create(axes), Write(x_label), Write(y_label))
        for graph, label in zip(graphs, labels):
            self.play(Create(graph), Write(label))

        self.wait(2)
