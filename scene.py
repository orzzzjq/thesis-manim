from manim import *
from manim_slides import Slide, ThreeDSlide
import pd
import sib
import sebb

def LatexPreamble():
    preamble = TexTemplate()
    preamble.add_to_preamble(r'''
        \usepackage{amsmath}
        \usepackage{amssymb}
        \usepackage{amsfonts}
        \usepackage{bm}
        \usepackage{bbm}
        \usepackage{xcolor}
        \usepackage{graphicx}
        \usepackage{ctable}
        \usepackage{multirow}
        \usepackage{multicol}
        \usepackage{ragged2e}
        \usepackage[cal=boondoxo]{mathalfa}
        \DeclareFontFamily{U}{FdSymbolA}{}
        \DeclareFontShape{U}{FdSymbolA}{m}{n}{<-> s * [1] FdSymbolA-Book}{}
        \DeclareFontShape{U}{FdSymbolA}{m}{b}{<-> s * [1] FdSymbolA-Medium}{}
        \DeclareSymbolFont{fdsymbols}{U}{FdSymbolA}{m}{n}
        \SetSymbolFont{fdsymbols}{bold}{U}{FdSymbolA}{m}{b}
        \DeclareMathSymbol{\bdiamond}{\mathbin}{fdsymbols}{130}
        \DeclareMathOperator*{\conv}{{\bf conv}}
        \DeclareMathOperator*{\dist}{{\bf dist}}
        \DeclareMathOperator*{\bary}{{\bf bary}}
        \DeclareMathOperator*{\diag}{{\bf diag}}
        \DeclareMathOperator*{\vecc}{{\bf vec}}
        \DeclareMathOperator*{\matt}{{\bf mat}}
        \DeclareMathOperator*{\subto}{subject\ to}
        \DeclareMathOperator*{\maximize}{maximize}
        \DeclareMathOperator*{\minimize}{minimize}
        \DeclareMathOperator*{\argmax}{argmax}
        \DeclareMathOperator*{\argmin}{argmin}
        \newcommand{\Oplus}{\ensuremath{\vcenter{\hbox{\scalebox{1.2}{$\oplus$}}}}}
        \newcommand{\medcap}{\ensuremath{\vcenter{\hbox{\scalebox{1.2}{$\cap$}}}}}
        \DeclareMathOperator*{\cproduct}{\operatorname*{\Oplus}}
        \newcommand{\OPT}{{\sf OPT}}
        \newcommand{\eps}{\varepsilon}
        \newcommand{\Tr}{\mathbf{tr}}
        \newcommand{\mm}[1]{{\boldsymbol{#1}}}
        \newcommand{\bb}[1]{\mathbbm{#1}}
        \newcommand{\cc}[1]{\mathcal{#1}}
        \newcommand{\xt}[2]{{#1}^{(#2)}}
        \newcommand{\eigen}[2]{\lambda_{#1}({#2})}
        \newcommand{\eigenval}[2]{\lambda_{#1}({#2})}
        \newcommand{\inprod}[2]{{\langle{#1}, {#2}\rangle}}
        \newcommand{\mmexp}{\mathbf{exp}}
        \newcommand{\mmint}{\mathbf{int}}
        \newcommand{\mmdiag}{\mathbf{diag}}
        \newcommand{\bA}{\bb{A}}
        \newcommand{\bB}{\bb{B}}
        \newcommand{\bC}{\bb{C}}
        \newcommand{\bD}{\bb{D}}
        \newcommand{\bE}{\bb{E}}
        \newcommand{\bF}{\bb{F}}
        \newcommand{\bG}{\bb{G}}
        \newcommand{\bH}{\bb{H}}
        \newcommand{\bI}{\bb{I}}
        \newcommand{\bJ}{\bb{J}}
        \newcommand{\bK}{\bb{K}}
        \newcommand{\bL}{\bb{L}}
        \newcommand{\bM}{\bb{M}}
        \newcommand{\bN}{\bb{N}}
        \newcommand{\bO}{\bb{O}}
        \newcommand{\bP}{\bb{P}}
        \newcommand{\bQ}{\bb{Q}}
        \newcommand{\bR}{\bb{R}}
        \newcommand{\bS}{\bb{S}}
        \newcommand{\bT}{\bb{T}}
        \newcommand{\bU}{\bb{U}}
        \newcommand{\bV}{\bb{V}}
        \newcommand{\bW}{\bb{W}}
        \newcommand{\bX}{\bb{X}}
        \newcommand{\bY}{\bb{Y}}
        \newcommand{\bZ}{\bb{Z}}
        \newcommand{\mma}{\mm{a}}
        \newcommand{\mmb}{\mm{b}}
        \newcommand{\mmc}{\mm{c}}
        \newcommand{\mmd}{\mm{d}}
        \newcommand{\mme}{\mm{e}}
        \newcommand{\mmf}{\mm{f}}
        \newcommand{\mmg}{\mm{g}}
        \newcommand{\mmh}{\mm{h}}
        \newcommand{\mmi}{\mm{i}}
        \newcommand{\mmj}{\mm{j}}
        \newcommand{\mmk}{\mm{k}}
        \newcommand{\mml}{\mm{l}}
        \newcommand{\mmm}{\mm{m}}
        \newcommand{\mmn}{\mm{n}}
        \newcommand{\mmo}{\mm{o}}
        \newcommand{\mmp}{\mm{p}}
        \newcommand{\mmq}{\mm{q}}
        \newcommand{\mmr}{\mm{r}}
        \newcommand{\mms}{\mm{s}}
        \newcommand{\mmt}{\mm{t}}
        \newcommand{\mmu}{\mm{u}}
        \newcommand{\mmv}{\mm{v}}
        \newcommand{\mmw}{\mm{w}}
        \newcommand{\mmx}{\mm{x}}
        \newcommand{\mmy}{\mm{y}}
        \newcommand{\mmz}{\mm{z}}
        \newcommand{\mmA}{\mm{A}}
        \newcommand{\mmB}{\mm{B}}
        \newcommand{\mmC}{\mm{C}}
        \newcommand{\mmD}{\mm{D}}
        \newcommand{\mmE}{\mm{E}}
        \newcommand{\mmF}{\mm{F}}
        \newcommand{\mmG}{\mm{G}}
        \newcommand{\mmH}{\mm{H}}
        \newcommand{\mmI}{\mm{I}}
        \newcommand{\mmJ}{\mm{J}}
        \newcommand{\mmK}{\mm{K}}
        \newcommand{\mmL}{\mm{L}}
        \newcommand{\mmM}{\mm{M}}
        \newcommand{\mmN}{\mm{N}}
        \newcommand{\mmO}{\mm{O}}
        \newcommand{\mmP}{\mm{P}}
        \newcommand{\mmQ}{\mm{Q}}
        \newcommand{\mmR}{\mm{R}}
        \newcommand{\mmS}{\mm{S}}
        \newcommand{\mmT}{\mm{T}}
        \newcommand{\mmU}{\mm{U}}
        \newcommand{\mmV}{\mm{V}}
        \newcommand{\mmW}{\mm{W}}
        \newcommand{\mmX}{\mm{X}}
        \newcommand{\mmY}{\mm{Y}}
        \newcommand{\mmZ}{\mm{Z}}
        \newcommand{\mmgamma}{{\boldsymbol{\gamma}}}
        \newcommand{\mmlambda}{{\boldsymbol{\lambda}}}
        \newcommand{\mmmu}{{\boldsymbol{\mu}}}
        \newcommand{\mmxi}{{\boldsymbol{\xi}}}
        \newcommand{\mmeta}{{\boldsymbol{\eta}}}
        \newcommand{\mmpsi}{{\boldsymbol{\psi}}}
        \newcommand{\mmone}{\mm{1}}
        \newcommand{\mmzero}{\mm{0}}
        \newcommand{\brmf}{{\rm\bf f}}

        \setlength{\parindent}{0pt}
        \usepackage{enumitem}
        \newlist{myitemize}{itemize}{2}
        \setlist[myitemize,1]{label=\textbullet,leftmargin=10pt,itemsep=.5em}
        \setlist[myitemize,2]{label=$\blacktriangleright$,leftmargin=20pt,itemsep=.5em}

        \usepackage{pmboxdraw}
        \usepackage{newunicodechar}
        \newunicodechar{└}{\textSFii}
        \newunicodechar{├}{\textSFviii}
        \newunicodechar{─}{\textSFx}
    ''')
    return preamble

def TitlePage():
    title = VGroup(
        Text("Efficient Algorithms for Geometric Optimization", t2c={"Efficient Algorithms" : RED, "Geometric Optimization" : BLUE}).scale(0.85),
        Text("and Symmetric Cone Programming", t2c={"Symmetric Cone Programming" : YELLOW}).scale(0.85),
    ).arrange(DOWN).shift(UP)
    name = Text("Jiaqi Zheng").scale(0.6).next_to(title, DOWN, buff=1.0)
    affliation = Text("Department of Computer Science, NUS").scale(0.5).next_to(name, DOWN, buff=0.5)
    date = Text("August 5, 2024").scale(0.5).next_to(affliation, DOWN, buff=0.25)
    return VGroup(title, name, affliation, date)

def DExperiments():
    pd = ImageMobject("pictures/experiments/pd_n_100k.png").shift(UP * 2)
    seb = ImageMobject("pictures/experiments/ses_n_100k.png").next_to(pd, DOWN, buff=0.1)
    pd_text = Text("PD/SVM").rotate(PI/2).next_to(pd, LEFT).scale(0.5)
    seb_text = Text("SEB").rotate(PI/2).next_to(seb, LEFT).scale(0.5)
    group = Group(pd,seb,pd_text,seb_text).scale(0.9)
    title = Text("Different Dimensionalities").rotate(PI/2).scale(0.6).next_to(group, LEFT)
    return Group(group, title)

def NExperiments():
    pd = ImageMobject("pictures/experiments/pd_d_64.png").shift(UP * 2)
    seb = ImageMobject("pictures/experiments/ses_d_64.png").next_to(pd, DOWN, buff=0.1)
    pd_text = Text("PD/SVM").rotate(PI/2).next_to(pd, LEFT).scale(0.5)
    seb_text = Text("SEB").rotate(PI/2).next_to(seb, LEFT).scale(0.5)
    group = Group(pd,seb,pd_text,seb_text).scale(0.9)
    title = Text("Different Input Sizes").rotate(PI/2).scale(0.6).next_to(group, LEFT)
    return Group(group, title)


# def OutlinePage():

def SubTitle(s):
    return Text(s).scale(0.6).to_edge(UL, buff=0.3)

class Presentation(Slide):
    def construct(self):
        preamble = LatexPreamble()
        def MyTex(s, up=None, buff=0.5):
            nonlocal preamble
            if up:
                return Tex(r'\justifying{' + s + r'}', tex_template=preamble).scale(0.7).next_to(up, DOWN, buff=buff).to_edge(LEFT, buff=1)
            else:
                return Tex(r'\justifying{' + s + r'}', tex_template=preamble).scale(0.7)

        def Theorem(s, up=None, buff=0.5, edge_color=RED):
            tex = MyTex(s)
            width, height = tex.width + 0.5, tex.height + 0.5
            rect = Rectangle(height=height, width=width, color=edge_color)
            group = Group(rect, tex)
            if up:
                return group.next_to(up, DOWN, buff=buff)
            return group

        def GeometrySummary():
            nonlocal preamble
            return Tex(r'''
            \begin{table*}[b]
            \renewcommand{\arraystretch}{1.1}
            \begin{tabular}{|c|wl{6cm}|wc{3.2cm}|wc{2.8cm}|}
            \hline
            \multicolumn{2}{|c|}{Problem} & Previous Work & This Thesis \\ 
            \hline\hline
            \multicolumn{2}{|c|}{PD (Hard-SVM)} & \scalebox{.85}{$\widetilde{O}({R^2 (M + d)\over \eps^2})$~[CHW12]} & \scalebox{.85}{$\widetilde{O}({R^2(N+d) \over \eps^2})$} \\\hline
            \multicolumn{2}{|c|}{SEB of Balls (SEBB)} & \scalebox{.85}{${O}({nd \over \eps})$~[Yild08]} & \scalebox{.85}{$\widetilde{O}({nd \over \eps^2})$} \\\hline
            \parbox[t]{2mm}{\multirow{9}{*}{\rotatebox[origin=c]{90}{SIB of}}}
            & Convex Polytopes & \scalebox{.85}{$O(M)^\ddag$~[JMB96]} & \scalebox{.85}{$\widetilde{O}({R^2(N + nd) \over \eps^2})$} \\
            & ├─ PD (Hard-SVM) & \scalebox{.85}{$\widetilde{O}({R^2 (M + d)\over \eps^2})$~[CHW12]} & \scalebox{.85}{$O({R^2(N+d) \over \eps^2})$} \\
            & ├─ SEB of Points (Hard-SVDD) & \scalebox{.85}{$\widetilde{O}({n\over \eps^2} + {d \over \eps})$~[CHW12]} & \scalebox{.85}{$\widetilde{O}({nd \over \eps^2})$} \\
            & └─ Line Segments & \scalebox{.85}{$O(n)^\ddag$~[BJMR91]} & \scalebox{.85}{$\widetilde{O}({R^2 nd \over \eps^2})$} \\\cline{2-4}
            & Reduced Polytopes & - & \scalebox{.85}{$\widetilde{O}({R^2(N + nd) \over \eps^2})$} \\
            & └─ Soft-SVM ($C$-SVM, $\nu$-SVM) & \scalebox{.85}{$\widetilde{O}({R^2 (M + d)\over \eps^2})$~[HKS11]} & \scalebox{.85}{$O({R^2(N+d) \over \eps^2})$} \\\cline{2-4}
            & AABBs (Imprecise Points) & \scalebox{.85}{$O(n)^\ddag$~[LK10]} & \scalebox{.85}{$\widetilde{O}({R^2 nd \over \eps^2})$} \\\cline{2-4}
            & Balls (Imprecise Points) & \scalebox{.85}{$O({n \over \eps^{(d-1)/2}})$~[SA15]} & \scalebox{.85}{$\widetilde{O}({R^2 nd \over \eps^2})$} \\\cline{2-4}
            & Ellipsoids (Distributions) & - & \scalebox{.85}{$\widetilde{O}(nd^\omega + {R^2 nd^2 \over \eps^2})$} \\\hline
            \multicolumn{2}{|c|}{Soft-SIB of Points (Soft-SVDD)$^\dag$} & - & \scalebox{.85}{$\widetilde{O}({R^2 nd \over \eps^2})$} \\
            \hline
            \end{tabular}
            \end{table*}
            ''', tex_template=preamble).scale(0.625)

        # # Title Page ##################################################################################################
        title = TitlePage()
        self.add(title)
        self.wait()
        self.next_slide()
        self.remove(title)

        # Subtitles ###################################################################################################
        subtitle_eja = Text("Euclidean Jordan Algebra & Symmetric Cones")
        subtitle_game = Text("Zero-Sum Games in EJA")
        subtitle_geometry = Text("Geometric Optimization", color=BLUE)
        subtitle_scp = Text("Symmetric Cone Programming", color=YELLOW)
        subtitle_parallel = Text("Parallel Computing", color=RED)
        subtitle_conclu = Text("Conclusion & Future Directions")




#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
# Introduction ########################################################################################################
        intro_pos = {
            'circle_geometry' : UL * 1.2,
            'circle_scp' : UR * 1.2,
            'circle_parallel' : DOWN * 0.75 * 1.2,
            'subtitle_geometry' : UL * 2 + DOWN * 0.4,
            'subtitle_scp' : UR * 2 + DOWN * 0.4,
            'subtitle_parallel' : DOWN + DOWN * 0.8
        }
        for x in intro_pos.keys():
            intro_pos[x] += DOWN * 0.45

        intro_circle_geometry = Circle(radius=2.5, color=BLUE, fill_color=BLUE, fill_opacity=0.1)
        intro_circle_scp = Circle(radius=2.5, color=YELLOW, fill_color=YELLOW, fill_opacity=0.1)
        intro_circle_parallel = Circle(radius=2.5, color=RED, fill_color=RED, fill_opacity=0.1)
        intro_circle_group = Group(intro_circle_geometry, intro_circle_scp, intro_circle_parallel)

        intro_circle_geometry.move_to(intro_pos['circle_geometry'])
        intro_circle_scp.move_to(intro_pos['circle_scp'])
        intro_circle_parallel.move_to(intro_pos['circle_parallel'])

        self.play(
            GrowFromCenter(intro_circle_geometry),
            GrowFromCenter(intro_circle_scp),
            GrowFromCenter(intro_circle_parallel)
        )

        subtitle_geometry.move_to(intro_pos['subtitle_geometry']).set_font_size(25).rotate(PI / 3)
        subtitle_scp.move_to(intro_pos['subtitle_scp']).set_font_size(22).rotate(-PI / 3)
        subtitle_parallel.move_to(intro_pos['subtitle_parallel']).set_font_size(25)

        intro_group = Group(intro_circle_group, subtitle_geometry, subtitle_scp, subtitle_parallel)

        self.play(
            FadeIn(subtitle_geometry, subtitle_scp, subtitle_parallel)
        )

        self.wait()
        self.next_slide()

        ## Intro - Goemetric Optimization
        self.play(Rotate(intro_group, -PI/3, about_point=(intro_circle_geometry.get_center() + intro_circle_scp.get_center() + intro_circle_parallel.get_center())/3))

        intro_pos['circle_geometry'] = intro_circle_geometry.get_center()
        intro_pos['circle_scp'] = intro_circle_scp.get_center()
        intro_pos['circle_parallel'] = intro_circle_parallel.get_center()
        intro_pos['subtitle_geometry'] = subtitle_geometry.get_center()
        intro_pos['subtitle_scp'] = subtitle_scp.get_center()
        intro_pos['subtitle_parallel'] = subtitle_parallel.get_center()

        self.play(
            intro_circle_geometry.animate.scale(10).set_fill(None, opacity=0),
            subtitle_geometry.animate.set_font_size(30).to_edge(UP, buff=0.5),
            intro_circle_scp.animate.shift(DR * 10),
            subtitle_scp.animate.shift(DR * 10),
            intro_circle_parallel.animate.shift(DL * 10),
            subtitle_parallel.animate.shift(DL * 10)
        )


        intro_geometry_text = MyTex(r'''
        A geometric optimization problem is to find a geometric object of some type that is optimal according to \underline{some criterion}, among all objects of this type that satisfy \underline{a certain geometric condition}.
        ''')

        intro_geometry_text[0][1:22].set_color(BLUE)

        self.play(Create(intro_geometry_text))
        self.wait()
        self.next_slide()

        self.play(intro_geometry_text.animate.scale(0.6).next_to(subtitle_geometry, DOWN, buff=0.25), run_time=1)

        ## polytope distance & svm
        
        geometry_pd_p_hall = Polygon(*np.c_[pd.p_points_hall, np.zeros(pd.p_points_hall.shape[0])], color=YELLOW, fill_opacity=0.3)
        geometry_pd_q_hall = Polygon(*np.c_[pd.q_points_hall, np.zeros(pd.q_points_hall.shape[0])], color=BLUE, fill_opacity=0.3)

        geometry_pd_p_dots = [Dot([*pd.p_points[i], 0], color=YELLOW) for i in range(len(pd.p_points))]
        geometry_pd_q_dots = [Dot([*pd.q_points[i], 0], color=BLUE) for i in range(len(pd.q_points))]

        geometry_pd_p_dots_group = Group(*geometry_pd_p_dots)
        geometry_pd_q_dots_group = Group(*geometry_pd_q_dots)

        geometry_pd_p_tex = MyTex(r'$\cc{P}$').scale(1.5).next_to(geometry_pd_p_dots_group, DOWN, buff=0.25).set_color(YELLOW)
        geometry_pd_q_tex = MyTex(r'$\cc{Q}$').scale(1.5).next_to(geometry_pd_q_dots_group, DOWN, buff=0.25).set_color(BLUE)
        
        intro_pd_text = Text(r'Polytope Distance (PD)').set_font_size(32).set_color(RED).next_to(geometry_pd_q_tex, DOWN, buff=0.25)
        intro_pd_text.shift([-intro_pd_text.get_center()[0], 0, 0])

        geometry_pd_opt_line = Line(*pd.optimal_line_seg, color=RED)

        geometry_pd_draw_group = Group(intro_pd_text, geometry_pd_p_dots_group, geometry_pd_q_dots_group, geometry_pd_p_hall, geometry_pd_q_hall, geometry_pd_opt_line, geometry_pd_p_tex, geometry_pd_q_tex)

        ## support vector machine

        geometry_svm_p_dots_group = geometry_pd_p_dots_group.copy()
        geometry_svm_q_dots_group = geometry_pd_q_dots_group.copy()

        geometry_svm_p_hall = geometry_pd_p_hall.copy()
        geometry_svm_q_hall = geometry_pd_q_hall.copy()

        geometry_svm_p_tex = geometry_pd_p_tex.copy()
        geometry_svm_q_tex = geometry_pd_q_tex.copy()

        intro_svm_text = Text(r'Support Vector Machine (SVM)').set_font_size(32).set_color(RED).next_to(geometry_svm_q_tex, DOWN, buff=0.25)
        intro_svm_text.shift([-intro_svm_text.get_center()[0], 0, 0])

        geometry_svm_draw_subgroup = Group(
            geometry_svm_p_dots_group,
            geometry_svm_q_dots_group,
            geometry_svm_p_hall,
            geometry_svm_q_hall,
            geometry_svm_p_tex,
            geometry_svm_q_tex
        )

        geometry_svm_line = Line(*pd.optimal_svm_line, color=RED)
        geometry_svm_dashedline = [
            DashedLine(*pd.optimal_svm_line, color=RED).shift(LEFT * 0.75),
            DashedLine(*pd.optimal_svm_line, color=RED).shift(-LEFT * 0.75),
        ]

        geometry_svm_draw_group = Group(geometry_svm_draw_subgroup, geometry_svm_line, *geometry_svm_dashedline, intro_svm_text)

        ### animation

        #### polytope distance

        geometry_pd_draw_group.scale(0.8).next_to(intro_geometry_text, DOWN, buff=0.5)

        self.play(Create(geometry_pd_p_hall), Create(geometry_pd_q_hall))
        self.wait()
        self.next_slide()

        self.play(Create(geometry_pd_opt_line))
        self.wait()
        self.next_slide()

        self.play(Create(intro_pd_text))
        self.wait()
        self.next_slide()

        self.play(FadeIn(geometry_pd_p_dots_group, geometry_pd_q_dots_group, geometry_pd_p_tex, geometry_pd_q_tex))
        self.wait()
        self.next_slide()

        self.play(geometry_pd_draw_group.animate.scale(0.65 / 0.8).to_edge(LEFT, buff=0.5))

        #### svm

        geometry_svm_draw_group.scale(0.65).to_edge(RIGHT, buff=0.5)

        self.play(FadeIn(geometry_svm_draw_subgroup))
        self.play(Create(geometry_svm_line))
        self.play(
            FadeOut(geometry_svm_p_hall, geometry_svm_q_hall),
            FadeIn(*geometry_svm_dashedline, intro_svm_text)
        )
        self.wait()
        self.next_slide()

        self.play(
            FadeOut(
                geometry_svm_p_dots_group,
                geometry_svm_q_dots_group,
                geometry_svm_p_tex,
                geometry_svm_q_tex,
                geometry_svm_line, 
                *geometry_svm_dashedline, 
                intro_svm_text
            ),
            geometry_pd_draw_group.animate.scale(0.4).to_edge(UL, buff=0.4)
        )
        self.wait()
        self.next_slide()


        ## smallset enclosing ball
        
        geometry_draw_seb = Circle(radius=sebb.radius, color=RED, fill_opacity=0.3)
        intro_seb_text = Text('Smallset Enclosing Ball (SEB)').set_font_size(32).set_color(RED).next_to(geometry_draw_seb, DOWN, buff=0.5)
        
        geometry_draw_seb_group = Group(geometry_draw_seb, *sebb.objects, intro_seb_text)

        ### animation
        geometry_draw_seb_group.scale(0.8).next_to(intro_geometry_text, DOWN, buff=0.5)

        self.play(FadeIn(*sebb.objects))
        self.wait()
        self.next_slide()

        self.play(Create(geometry_draw_seb))
        self.play(Create(intro_seb_text))
        self.wait()
        self.next_slide()

        ### sebb

        self.play(FadeOut(geometry_draw_seb_group))

        geometry_draw_sebb = Circle(radius=2.75, color=RED, fill_opacity=0.3).move_to([0.28, -0.07, 0])
        intro_sebb_text = Text('SEB of Balls (SEBB)').set_font_size(32).set_color(RED).next_to(geometry_draw_sebb, DOWN, buff=0.5)
        geometry_draw_sebb_objects = [x.copy() for x in sib.objects]
        geometry_draw_sebb_group = Group(geometry_draw_sebb, *geometry_draw_sebb_objects, intro_sebb_text)

        #### animation
        geometry_draw_sebb_group.scale(0.8).next_to(intro_geometry_text, DOWN, buff=0.5)

        self.play(FadeIn(*geometry_draw_sebb_objects))
        self.wait()
        self.next_slide()

        self.play(Create(geometry_draw_sebb))
        self.play(Create(intro_sebb_text))
        self.wait()
        self.next_slide()

        self.play(
            geometry_draw_sebb_group.animate.scale(0.4 * 0.65 / 0.8).to_edge(UR, buff=0.4)
        )
        self.wait()
        self.next_slide()

        
        ## smallest intersecting ball

        geometry_draw_sib = Circle(radius=2, color=RED, fill_opacity=0.3)
        geometry_draw_sib_objects = [x.copy() for x in sib.objects]
        geometry_draw_sib_subgroup = Group(geometry_draw_sib, *geometry_draw_sib_objects)
        intro_sib_text = Text('Smallest Intersecting Ball (SIB)').set_font_size(32).set_color(RED).next_to(geometry_draw_sib_subgroup, DOWN, buff=0.5)
        geometry_draw_sib_group = Group(geometry_draw_sib_subgroup, intro_sib_text)

        #### animation
        geometry_draw_sib_group.scale(0.8).next_to(intro_geometry_text, DOWN, buff=0.5)

        self.play(FadeIn(*geometry_draw_sib_objects))
        self.wait()
        self.next_slide()

        self.play(Create(geometry_draw_sib))
        self.play(Create(intro_sib_text))
        self.wait()
        self.next_slide()

        self.play(
            geometry_draw_sib_group.animate.scale(0.4 * 0.65 / 0.8).next_to(geometry_pd_draw_group, DOWN, buff=0.25).to_edge(LEFT, buff=0.4)
        )
        self.wait()
        self.next_slide()
        
        
        ## Soft-SIB

        geometry_draw_soft_sib = Circle(radius=sib.soft_radius, color=RED, fill_opacity=0.3).shift(sib.soft_center)
        geometry_draw_soft_sib_margin = DashedVMobject(Circle(radius=sib.soft_margin_radius, color=RED, fill_opacity=0.3).shift(sib.soft_center))
        geometry_draw_soft_sib_objects = [x.copy() for x in sib.objects]
        geometry_draw_soft_sib_subgroup = Group(geometry_draw_soft_sib, *geometry_draw_soft_sib_objects, geometry_draw_soft_sib_margin)
        intro_soft_sib_text = Text('Soft-SIB').set_font_size(32).set_color(RED).next_to(geometry_draw_soft_sib_subgroup, DOWN, buff=0.5)
        geometry_draw_soft_sib_group = Group(geometry_draw_soft_sib_subgroup, intro_soft_sib_text)

        #### animation
        geometry_draw_soft_sib_group.scale(0.8).next_to(intro_geometry_text, DOWN, buff=0.5)

        self.play(FadeIn(*geometry_draw_soft_sib_objects))
        self.wait()
        self.next_slide()

        self.play(Create(geometry_draw_soft_sib))
        self.play(FadeIn(geometry_draw_soft_sib_margin))
        self.play(Create(intro_soft_sib_text))
        self.wait()
        self.next_slide()

        geometry_intro_list = [
            geometry_pd_draw_group.copy(),
            geometry_draw_sebb_group.copy(),
            geometry_draw_sib_group.copy(),
            geometry_draw_soft_sib_group.copy().scale(0.4 * 0.65 / 0.8)
        ]

        geometry_intro_list[1].next_to(geometry_intro_list[0], RIGHT, buff=1)
        geometry_intro_list[3].next_to(geometry_intro_list[1], DOWN, buff=0.25)
        geometry_intro_list[2].move_to([geometry_intro_list[0].get_center()[0], geometry_intro_list[3].get_center()[1], 0])

        geometry_intro_hidden_group = Group(*geometry_intro_list)

        geometry_intro_hidden_group.scale(1.5).next_to(intro_geometry_text, DOWN, buff=0.25)

        # self.add(geometry_intro_hidden_group)

        self.play(
            geometry_pd_draw_group.animate.scale(1.5).move_to(geometry_intro_list[0].get_center()),
            geometry_draw_sebb_group.animate.scale(1.5).move_to(geometry_intro_list[1].get_center()),
            geometry_draw_sib_group.animate.scale(1.5).move_to(geometry_intro_list[2].get_center()),
            geometry_draw_soft_sib_group.animate.scale(0.4 * 0.65 * 1.5 / 0.8).move_to(geometry_intro_list[3].get_center())
        )
        self.wait()
        self.next_slide()

        self.play(
            FadeOut(
                intro_geometry_text,
                geometry_pd_draw_group,
                geometry_draw_sebb_group,
                geometry_draw_sib_group,
                geometry_draw_soft_sib_group
            )
        )


        ## Intro - Symmetric Cone Programming
        self.play(
            intro_circle_geometry.animate.scale(1 / 10).set_fill(BLUE, opacity=0.1),
            subtitle_geometry.animate.set_font_size(25).move_to(intro_pos['subtitle_geometry']),
            intro_circle_scp.animate.move_to(intro_pos['circle_scp']),
            subtitle_scp.animate.move_to(intro_pos['subtitle_scp']),
            intro_circle_parallel.animate.move_to(intro_pos['circle_parallel']),
            subtitle_parallel.animate.move_to(intro_pos['subtitle_parallel'])
        )

        self.next_slide()

        self.play(Rotate(intro_group, PI* 2 / 3, about_point=(intro_circle_geometry.get_center() + intro_circle_scp.get_center() + intro_circle_parallel.get_center())/3))

        intro_pos['circle_geometry'] = intro_circle_geometry.get_center()
        intro_pos['circle_scp'] = intro_circle_scp.get_center()
        intro_pos['circle_parallel'] = intro_circle_parallel.get_center()
        intro_pos['subtitle_geometry'] = subtitle_geometry.get_center()
        intro_pos['subtitle_scp'] = subtitle_scp.get_center()
        intro_pos['subtitle_parallel'] = subtitle_parallel.get_center()

        self.play(
            intro_circle_geometry.animate.shift(DR * 10),
            subtitle_geometry.animate.shift(DR * 10),
            intro_circle_scp.animate.scale(10).set_fill(None, opacity=0),
            subtitle_scp.animate.set_font_size(30).to_edge(UP, buff=0.5),
            intro_circle_parallel.animate.shift(DL * 10),
            subtitle_parallel.animate.shift(DL * 10)
        )


        intro_scp_text = MyTex(r'''\parbox{15cm}{
        A symmetric cone program is a \underline{linear optimization} problem over a \underline{symmetric cone}.
        }''')
        intro_scp_text[0][1:21].set_color(YELLOW)

        self.play(Create(intro_scp_text))
        self.wait()
        self.next_slide()

        self.play(intro_scp_text.animate.scale(0.65).next_to(subtitle_scp, DOWN, buff=0.25), run_time=1)

        intro_scp_formulation = [
            MyTex(r'''
            $\displaystyle
            \begin{aligned}
            \minimize \quad & \mmc^T \mmx \\
            \subto \quad & \mmA \mmx - \mmb \in \cc{K}
            \end{aligned}
            $
            ''')
        ]

        self.play(FadeIn(intro_scp_formulation[-1]))
        self.wait()
        self.next_slide()
        
        intro_scp_formulation.append(
            Text('Primal').set_font_size(24).set_color(RED).next_to(intro_scp_formulation[-1], UP, buff=0.25)
        )

        intro_scp_primal_group = Group(intro_scp_formulation[-1], intro_scp_formulation[-2])

        self.play(FadeIn(intro_scp_formulation[-1]))
        self.wait()
        self.next_slide()

        intro_scp_formulation.append(
            MyTex(r'''
            $\displaystyle
            \begin{aligned}
            \maximize \quad & \mmb \bullet \mmy \\
            \subto \quad & \mma_j \bullet \mmy = c_j,\ \forall j \in [m],\\
            & \mmy \in \cc{K}
            \end{aligned}
            $
            ''')
        )
        
        intro_scp_formulation.append(
            Text('Dual').set_font_size(24).set_color(RED).next_to(intro_scp_formulation[-1], UP, buff=0.25)
        )

        self.play(intro_scp_primal_group.animate.shift(LEFT * 3))

        intro_scp_dual_group = Group(intro_scp_formulation[-1], intro_scp_formulation[-2]).next_to(intro_scp_primal_group, RIGHT, buff=1)
        intro_scp_dual_group.shift([0, intro_scp_primal_group.get_top()[1] - intro_scp_dual_group.get_top()[1], 0])

        self.play(FadeIn(intro_scp_dual_group))
        self.wait()
        self.next_slide()

        intro_scp_group = Group(intro_scp_primal_group, intro_scp_dual_group)

        self.play(
            intro_scp_group.animate.scale(0.7).next_to(intro_scp_text, DOWN, buff=0.25)
        )
        self.wait()
        self.next_slide()

        intro_scp_examples = [
            MyTex(r'''
            $\displaystyle
            \begin{gathered}
            \text{Linear Program}\\
            \begin{aligned}[t]
            \minimize \quad & \mmc^T \mmx \\
            \subto \quad & \mmA \mmx - \mmb \ge 0
            \end{aligned}
            \hspace{3em}
            \begin{aligned}[t]
            \maximize \quad & \mmb^T \mmy \\
            \subto \quad & \mmA^T \mmy = \mmc, \\
            & \mmy \ge 0
            \end{aligned}
            \end{gathered}
            $
            ''').next_to(intro_scp_group, DOWN, buff=1)
        ]

        intro_scp_examples[-1][0][:13].set_color(BLUE)

        self.play(FadeIn(intro_scp_examples[-1]))
        self.wait()
        self.next_slide()

        intro_scp_examples.append(
            MyTex(r'''
            $\displaystyle
            \begin{gathered}
            \text{Semidefinite Program}\\
            \begin{aligned}[t]
            \minimize \quad & \mmc^T \mmx \\
            \subto \quad & \sum_{j=1}^m \mmA_j x_j - \mmB \succeq 0
            \end{aligned}
            \hspace{3em}
            \begin{aligned}[t]
            \maximize \quad & \Tr(\mmB \mmY) \\
            \subto \quad & \Tr(\mmA_j \mmY) = c_j,\ \forall j \in [m], \\
            & \mmY \succeq 0
            \end{aligned}
            \end{gathered}
            $
            ''').next_to(intro_scp_group, DOWN, buff=1)
        )

        intro_scp_examples[-1][0][:18].set_color(BLUE)

        self.play(FadeIn(intro_scp_examples[-1]), FadeOut(intro_scp_examples[-2]))
        self.wait()
        self.next_slide()

        intro_scp_examples.append(
            MyTex(r'''
            $\displaystyle
            \begin{gathered}
            \text{Second-Order Cone Program}\\
            \begin{aligned}[t]
            \maximize \quad & \mmc^T \mmx \\
            \subto \quad & \mmA_i \mmx - \mmb_i \in \cc{Q}^{d_i + 1},\ \forall i \in [n] \\
            \end{aligned}
            \hspace{3em}
            \begin{aligned}[t]
            \minimize \quad & \mmb_1^T \mmy_1 + \dots + \mmb_n^T \mmy_n \\
            \subto \quad & \mmA_1^T \mmy_1 + \dots + \mmA_n^T \mmy_n = \mmc, \\
            & \mmy_i \in \cc{Q}^{d_i + 1}, \ \forall i \in [n]
            \end{aligned}
            \end{gathered}
            $
            ''').next_to(intro_scp_group, DOWN, buff=1)
        )

        intro_scp_examples[-1][0][:23].set_color(BLUE)

        self.play(FadeIn(intro_scp_examples[-1]), FadeOut(intro_scp_examples[-2]))
        self.wait()
        self.next_slide()

        self.play(
            FadeOut(intro_scp_examples[-1]),
            intro_scp_group.animate.scale(1 / 0.7).move_to([0,0,0])
        )
        self.wait()
        self.next_slide()
        
        self.play(FadeOut(intro_scp_group, intro_scp_text))

        ## Intro - Parallel Computing
        self.play(
            intro_circle_geometry.animate.move_to(intro_pos['circle_geometry']),
            subtitle_geometry.animate.move_to(intro_pos['subtitle_geometry']),
            intro_circle_scp.animate.scale(1 / 10).set_fill(YELLOW, opacity=0.1),
            subtitle_scp.animate.set_font_size(22).move_to(intro_pos['subtitle_scp']),
            intro_circle_parallel.animate.move_to(intro_pos['circle_parallel']),
            subtitle_parallel.animate.move_to(intro_pos['subtitle_parallel'])
        )

        self.next_slide()

        self.play(Rotate(intro_group, - PI / 3, about_point=(intro_circle_geometry.get_center() + intro_circle_scp.get_center() + intro_circle_parallel.get_center())/3))

        intro_pos['circle_geometry'] = intro_circle_geometry.get_center()
        intro_pos['circle_scp'] = intro_circle_scp.get_center()
        intro_pos['circle_parallel'] = intro_circle_parallel.get_center()
        intro_pos['subtitle_geometry'] = subtitle_geometry.get_center()
        intro_pos['subtitle_scp'] = subtitle_scp.get_center()
        intro_pos['subtitle_parallel'] = subtitle_parallel.get_center()

        self.play(
            intro_circle_geometry.animate.shift(UL * 10),
            subtitle_geometry.animate.shift(UL * 10),
            intro_circle_scp.animate.shift(UR * 10),
            subtitle_scp.animate.shift(UR * 10),
            intro_circle_parallel.animate.scale(10).set_fill(None, opacity=0),
            subtitle_parallel.animate.set_font_size(30).to_edge(UP, buff=0.5)
        )

        self.next_slide()

        intro_parallel_text = MyTex(r'''
            Why did we start to investigate these problems?
        ''')

        self.play(Create(intro_parallel_text))
        self.wait()
        self.next_slide()

        self.play(FadeOut(intro_parallel_text))

        intro_parallel_gpu = [
            MyTex(r'''GPU Computing''').set_color(RED)
        ]
        intro_parallel_geo = [
            MyTex(r'''Geometry''').set_color(RED)
        ]
        intro_parallel_opt = [
            MyTex(r'''Optimization''').set_color(RED)
        ]
        
        intro_parallel_gpu[0].next_to(subtitle_parallel, DOWN, buff=0.25)
        intro_parallel_geo[0].shift(LEFT * 3)
        intro_parallel_opt[0].shift(RIGHT * 3)
        
        intro_parallel_titles = [intro_parallel_gpu[0], intro_parallel_geo[0], intro_parallel_opt[0]]

        intro_parallel_arrows = [
            Arrow(intro_parallel_titles[0].get_left(), intro_parallel_titles[1].get_center(), buff=0.5, stroke_width=8),    # 0: gpu -> geo
            Arrow(intro_parallel_titles[0].get_right(), intro_parallel_titles[2].get_center(), buff=0.5, stroke_width=8),   # 1: gpu -> opt
            Arrow(intro_parallel_titles[1].get_center(), intro_parallel_titles[0].get_left(), buff=0.5, stroke_width=8),    # 2: geo -> gpu
            Arrow(intro_parallel_titles[1].get_right(), intro_parallel_titles[2].get_left(), buff=1, stroke_width=8),       # 3: geo -> opt
            Arrow(intro_parallel_titles[2].get_center(), intro_parallel_titles[0].get_right(), buff=0.5, stroke_width=8),   # 4: opt -> gpu
            Arrow(intro_parallel_titles[2].get_left(), intro_parallel_titles[1].get_right(), buff=1, stroke_width=8)        # 5: opt -> geo
        ]

        self.play(FadeIn(intro_parallel_gpu[0], intro_parallel_geo[0], intro_parallel_opt[0]))
        self.wait()
        self.next_slide()

        intro_parallel_gpu.append(MyTex(r'Some attempts on LP').next_to(intro_parallel_gpu[-1], DOWN, buff=0.25).scale(0.95)) # 1
        intro_parallel_gpu.append(MyTex(r'Some attempts on PosLP').next_to(intro_parallel_gpu[-1], DOWN, buff=0.1).scale(0.95)) # 2
        intro_parallel_gpu.append(MyTex(r'Implementation for PD').next_to(intro_parallel_gpu[-1], DOWN, buff=0.1).scale(0.95).set_color(YELLOW)) # 3
        intro_parallel_gpu.append(MyTex(r'Implementation for SEB').next_to(intro_parallel_gpu[-1], DOWN, buff=0.1).scale(0.95).set_color(YELLOW)) # 4

        intro_parallel_geo.append(MyTex(r'Centroidal Voronoi diagram').next_to(intro_parallel_geo[-1], DOWN, buff=0.25).scale(0.95)) # 1
        intro_parallel_geo.append(MyTex(r"Megiddo's algorithm").next_to(intro_parallel_geo[-1], DOWN, buff=0.1).scale(0.95)) # 2
        intro_parallel_geo.append(MyTex(r'Polytope distance').next_to(intro_parallel_geo[-1], DOWN, buff=0.1).scale(0.95).set_color(YELLOW)) # 3
        intro_parallel_geo.append(MyTex(r'Smallest enclosing ball').next_to(intro_parallel_geo[-1], DOWN, buff=0.1).scale(0.95).set_color(YELLOW)) # 4
        intro_parallel_geo.append(MyTex(r'Smallest intersecting ball').next_to(intro_parallel_geo[-1], DOWN, buff=0.1).scale(0.95).set_color(YELLOW)) # 5
        intro_parallel_geo.append(MyTex(r'Soft-SIB').next_to(intro_parallel_geo[-1], DOWN, buff=0.1).scale(0.95).set_color(YELLOW)) # 6

        intro_parallel_opt.append(MyTex(r'Linear program').next_to(intro_parallel_opt[-1], DOWN, buff=0.25).scale(0.95)) # 1
        intro_parallel_opt.append(MyTex(r'Parallel algos for positive LP').next_to(intro_parallel_opt[-1], DOWN, buff=0.1).scale(0.95)) # 2
        intro_parallel_opt.append(MyTex(r'MMWU for approximating SDP').next_to(intro_parallel_opt[-1], DOWN, buff=0.1).scale(0.95)) # 3
        intro_parallel_opt.append(MyTex(r'MWU over symmetric cones').next_to(intro_parallel_opt[-1], DOWN, buff=0.1).scale(0.95)) # 4
        intro_parallel_opt.append(MyTex(r'SCMWU for approximating SCP').next_to(intro_parallel_opt[-1], DOWN, buff=0.1).scale(0.95).set_color(YELLOW)) # 5
        intro_parallel_opt.append(MyTex(r'SCMWU for zero-sum game').next_to(intro_parallel_opt[-1], DOWN, buff=0.1).scale(0.95).set_color(YELLOW)) # 6

        # gCVT
        self.play(
            Create(intro_parallel_arrows[0])
        )
        self.wait()
        self.next_slide()
        
        self.play(
            FadeIn(intro_parallel_geo[1])
        )
        self.wait()
        self.next_slide()

        # LP
        self.play(FadeOut(intro_parallel_arrows[0]))
        self.play(
            Create(intro_parallel_arrows[1]), Create(intro_parallel_arrows[3]),
            FadeIn(intro_parallel_opt[1])
        )
        self.wait()
        self.next_slide()

        self.play(
            FadeIn(intro_parallel_geo[2])
        )
        self.wait()
        self.next_slide()

        self.play(
            FadeIn(intro_parallel_gpu[1])
        )
        self.wait()
        self.next_slide()

        # Positive LP
        self.play(
            FadeOut(intro_parallel_arrows[1], intro_parallel_arrows[3]),
            FadeIn(intro_parallel_opt[2])
        )
        self.wait()
        self.next_slide()

        self.play(
            Create(intro_parallel_arrows[4]),
            FadeIn(intro_parallel_gpu[2])
        )
        self.wait()
        self.next_slide()

        self.play(
            FadeOut(intro_parallel_arrows[4])
        )
        self.play(
            Create(intro_parallel_arrows[1])
        )
        self.wait()
        self.next_slide()

        # Opt
        self.play(
            FadeOut(intro_parallel_arrows[1])
        )
        self.play(
            FadeIn(intro_parallel_opt[3])
        )
        self.wait()
        self.next_slide()

        self.play(
            FadeIn(intro_parallel_opt[4])
        )
        self.wait()
        self.next_slide()

        self.play(
            FadeIn(intro_parallel_opt[5])
        )
        self.wait()
        self.next_slide()

        # pd, seb
        self.play(
            Create(intro_parallel_arrows[5])
        )
        self.play(
            FadeIn(intro_parallel_geo[3], intro_parallel_geo[4])
        )
        self.wait()
        self.next_slide()

        # pd, seb, gpu
        self.play(
            FadeOut(intro_parallel_arrows[5])
        )
        self.play(
            Create(intro_parallel_arrows[2]),
            Create(intro_parallel_arrows[4])
        )
        self.play(
            FadeIn(intro_parallel_gpu[3], intro_parallel_gpu[4])
        )
        self.wait()
        self.next_slide()

        # game
        self.play(
            FadeOut(intro_parallel_arrows[2]),
            FadeOut(intro_parallel_arrows[4])
        )
        self.play(
            FadeIn(intro_parallel_opt[6])
        )
        self.wait()
        self.next_slide()

        # sib
        self.play(
            Create(intro_parallel_arrows[5])
        )
        self.play(
            FadeIn(intro_parallel_geo[5], intro_parallel_geo[6])
        )
        self.wait()
        self.next_slide()

        self.play(
            FadeOut(intro_parallel_arrows[5])
        )
        self.wait()
        self.next_slide()

        self.play(FadeOut(
            *intro_parallel_geo,
            *intro_parallel_gpu,
            *intro_parallel_opt
        ))

        ## Intro - Ending
        self.play(
            intro_circle_geometry.animate.move_to(intro_pos['circle_geometry']),
            subtitle_geometry.animate.move_to(intro_pos['subtitle_geometry']),
            intro_circle_scp.animate.move_to(intro_pos['circle_scp']),
            subtitle_scp.animate.move_to(intro_pos['subtitle_scp']),
            intro_circle_parallel.animate.scale(1 / 10).set_fill(RED, opacity=0.1),
            subtitle_parallel.animate.set_font_size(25).move_to(intro_pos['subtitle_parallel'])
        )

        self.next_slide()
        self.play(FadeOut(intro_circle_group))

        # Outline #####################################################################################################
        # Euclidean Jordan Algebra & Symmetric Cones
        # Zero-Sum Game in EJA
        # Geometric Optimization
        # Symmetric Cone Programming
        # Parallel Computing
        # Conclusion and Future Directions

        self.play(
            subtitle_geometry.animate.rotate(-PI/3).set_font_size(25).move_to([0., 0.41891479, 0.]),
            subtitle_scp.animate.rotate(PI/3).set_font_size(25).move_to([0, -4.13218177e-01, 0]),
            subtitle_parallel.animate.move_to([0, -1.24814859e+00, 0])
        )

        outline_list = VGroup(
            subtitle_eja.set_font_size(25),
            subtitle_game.set_font_size(25),
            subtitle_geometry.set_font_size(25),
            subtitle_scp.set_font_size(25),
            subtitle_parallel.set_font_size(25),
            subtitle_conclu.set_font_size(25)
        ).arrange(DOWN, buff=0.5).scale(1)

        outline_pos = {
            'subtitle_eja' : subtitle_eja.get_center(),
            'subtitle_game' : subtitle_game.get_center(),
            'subtitle_geometry' : subtitle_geometry.get_center(),
            'subtitle_scp' : subtitle_scp.get_center(),
            'subtitle_parallel' : subtitle_parallel.get_center(),
            'subtitle_conclu' : subtitle_conclu.get_center()
        }

        outline_title = Text("Outline").scale(.8).next_to(outline_list, UP, buff=1)
        outline_group = Group(outline_title, outline_list)

        self.play(FadeIn(outline_title, subtitle_eja, subtitle_game, subtitle_conclu))
        self.wait()
        self.next_slide()




###########################################################################################################################
###########################################################################################################################
###########################################################################################################################
# EJA & Symmetric Cones ###################################################################################################

        self.play(subtitle_eja.animate.to_edge(UL, buff=0.5),
            FadeOut(outline_title, subtitle_game, subtitle_geometry, subtitle_scp, subtitle_parallel, subtitle_conclu)
        )

        self.next_slide()

        jordan_algebra_1 = MyTex(r'''Jordan algebra $(\bJ, \circ)$: a finite-dimensional vector space $\bJ$ 
        and a bilinear binary operation $\circ$ satisfying:
        \begin{enumerate}
            \item (Commutativity) $\mmx \circ\mmy = \mmy \circ \mmx$,
            \item (Jordan identity) $\mmx^2 \circ (\mmx \circ \mmy) = \mmx \circ (\mmx^2 \circ \mmy)$.
        \end{enumerate}
        ''', up=subtitle_eja)
        jordan_algebra_1[0][0:19].set_color(BLUE)

        jordan_algebra_2 = MyTex(r'''
        Identity element: $\mmx \circ \mme = \mme \circ \mmx = \mmx$ for all $\mmx\in \bJ$
        ''', up=jordan_algebra_1)
        jordan_algebra_2[0][0:16].set_color(YELLOW)        

        jordan_algebra_3 = MyTex(r'''
        Powers: $\mmx^0 \triangleq \mme, \quad \mmx^k \triangleq \mmx\circ \mmx^{k-1},\ \forall k \ge 1$
        ''', up=jordan_algebra_2, buff=0.3)
        jordan_algebra_3[0][:7].set_color(YELLOW)

        jordan_algebra_4 = MyTex(r'''
        Degree of $\mmx$: the smallest $k\in \mathbbm{Z}_+$ such that $\mme, \mmx, \dots, \mmx^k$ are linearly dependent 
        ''', up=jordan_algebra_3, buff=0.3)
        jordan_algebra_4[0][:10].set_color(YELLOW)

        jordan_algebra_5 = MyTex(r'''
        Rank of $\bJ$: the largest degree of all $\mmx \in \bJ$
        ''', up=jordan_algebra_4, buff=0.3)
        jordan_algebra_5[0][:8].set_color(YELLOW)

        self.play(FadeIn(jordan_algebra_1))
        self.next_slide()

        self.play(FadeIn(jordan_algebra_2, jordan_algebra_3, jordan_algebra_4, jordan_algebra_5))
        self.next_slide()

        self.play(FadeOut(jordan_algebra_1, jordan_algebra_2, jordan_algebra_3, jordan_algebra_4, jordan_algebra_5))

        eja_1 = MyTex(r'''
        Euclidean Jordan algebra $(\bJ, \circ, \bullet)$: a Jordan algebra endowed with an inner product 
        $\bullet: \bJ \times \bJ \rightarrow \bR$ satisfying
        \[
        \mmx \bullet (\mmy \circ \mmz) = (\mmx \circ \mmy) \bullet \mmz, \quad \forall \mmx, \mmy, \mmz\in \bJ
        \]
        ''', up=subtitle_eja)
        eja_1[0][:30].set_color(BLUE)

        eja_2 = MyTex(r'''
        Spectral decomposition: 
        \[ \mmx = \sum_{k=1}^r \lambda_k(\mmx)\mmq_k, \]
        where $\lambda_1(\mmx), \dots, \lambda_r(\mmx)\in \bR$ are eigenvalues, and $\mmq_1,\dots, \mmq_r \in \bJ$ 
        are primitive orthogonal {\em idempotents} (or eigenvectors) satisfying:
        \begin{enumerate}
            \item (Idempotents and primitiveness) $\mmq_k^2 = \mmq_k$ and $\mmq_k\bullet \mmq_k = 1$, $\forall k \in [r]$,
            \item (Orthogonality) $\mmq_i \circ \mmq_j = 0,\ \forall i \neq j,\ i,j\in [r]$,
            \item (Completeness) $\sum_{k=1}^r \mmq_k = \mme$.
        \end{enumerate}
        ''', up=eja_1)
        eja_2[0][:22].set_color(YELLOW)
        eja_2[0][62:73].set_color(RED)
        eja_2[0][124:136].set_color(RED)

        self.play(FadeIn(eja_1))
        self.next_slide()

        self.play(FadeIn(eja_2))
        self.next_slide()

        eja_3 = MyTex(r'''
        Trace, determinant, and exponential:
        \[
            \Tr(\mmx) \triangleq \sum_{k=1}^r \lambda_k(\mmx), \quad {\bf det}(\mmx) \triangleq \prod_{k=1}^r \lambda_k(\mmx) \quad \text{and} \quad
            \mmexp(\mmx) \triangleq \sum_{k=1}^r \exp(\lambda_k(\mmx))\mmq_k
        \]
        ''', up=subtitle_eja)
        eja_3[0][:33].set_color(YELLOW)

        self.play(FadeOut(eja_1, eja_2))
        self.play(FadeIn(eja_3))
        self.next_slide()

        eja_4 = MyTex(r'''
        Infinity norm: $\|\mmx\|_\infty = \max_{k} |\lambda_k(\mmx)|$
        ''', up=eja_3)
        eja_4[0][:12].set_color(YELLOW)

        self.play(FadeIn(eja_4))

        eja_5 = MyTex(r'''
        Trace inner product: $\mmx\bullet \mmy = \Tr(\mmx \circ \mmy)$
        ''', up=eja_4)
        eja_5[0][:18].set_color(YELLOW)

        self.play(FadeIn(eja_5))

        eja_6 = MyTex(r'''
        Golden-Thompson inequality: 
        \[\Tr(\mmexp(\mmx + \mmy)) \le \Tr(\mmexp(\mmx)\circ\mmexp(\mmy)) = \mmexp(\mmx)\bullet \mmexp(\mmy)\]
        ''', up=eja_5)
        eja_6[0][:26].set_color(YELLOW)

        self.play(FadeIn(eja_6))
        self.next_slide()

        self.play(FadeOut(eja_3, eja_4, eja_5, eja_6))

        sc_1 = MyTex(r'''
        Symmetric cones are convex cones that are {\em self-dual} and {\em homogeneous}:
        \begin{itemize}
        \item $\cc{K} = \cc{K}^*$, where $\cc{K}^* = \big\{\mmy \in \bJ : \forall \mmx \in \cc{K},\ \mmx \bullet \mmy\ge 0 \big\}$
        \item There exists invertible operators $\cc{T}$ such that $\cc{T}(\cc{K}) = \cc{K}$
        \end{itemize}
        ''', up=subtitle_eja)
        sc_1[0][:14].set_color(BLUE)
        sc_1[0][35:44].set_color(RED)
        sc_1[0][47:58].set_color(RED)
        sc_1[0][60:64].set_color(RED)
        sc_1[0][-6:].set_color(RED)

        self.play(FadeIn(sc_1))
        self.next_slide()

        sc_2 = MyTex(r'''
        Jordan algebraic characterization of symmetric cones: 
        \begin{itemize}
        \item (Cone of squares) $\cc{K} = \big\{\mmx^2 : \mmx \in \bJ \big\}$
        \item (Cone of positivity) $\cc{K} = \big\{\mmx \in \bJ : \lambda_{\min}(\mmx) \ge 0 \big\}$
        \end{itemize}
        ''', up=sc_1)
        sc_2[0][:31].set_color(BLUE)
        sc_2[0][49:64].set_color(YELLOW)
        sc_2[0][75:93].set_color(YELLOW)

        self.play(FadeIn(sc_2))
        self.next_slide()

        sc_3 = MyTex(r'''
        Examples of symmetric cones: nonnegative orthant $\bR^n_+$, cone of real symmetric 
        PSD matrices $\cc{S}^n_+$, second-order cones $\cc{Q}^{d+1}$, and their Cartesian products
        ''', up=sc_2)
        sc_3[0][:25].set_color(BLUE)
        sc_3[0][43:46].set_color(YELLOW)
        sc_3[0][77:80].set_color(YELLOW)
        sc_3[0][98:102].set_color(YELLOW)
        sc_3[0][-17:].set_color(YELLOW)
        
        self.play(FadeIn(sc_3))
        self.next_slide()

        self.play(FadeOut(sc_1, sc_2, sc_3))

        sc_4 = MyTex(r'''
        Nonnegative orthant $\bR^n_+$:
        \begin{myitemize}
        \item[] Space: $\bJ = \bR^n$ \hspace{2em}
        Jordan product: $\mmx \circ \mmy = \diag(\mmx) \mmy$\\
        \vspace{-1.3em}
        \item[] Identity: $\mme = \mmone_n$ \hspace{1em}
        Trace: $\Tr(\mmx) = \sum_k x_k$ \hspace{1em}
        Inner product: $\mmx \bullet \mmy = \mmx^T \mmy$\\
        \vspace{-1.3em}
        \item[] Spectral decomposition: $\eigenval{k}{\mmx} = x_k,\ \mmq_k = \mme_k$\\
        \end{myitemize}
        ''', up=subtitle_eja)
        sc_4[0][:22].set_color(BLUE)
        sc_4[0][22:28].set_color(YELLOW)
        sc_4[0][32:46].set_color(YELLOW)
        sc_4[0][58:67].set_color(YELLOW)
        sc_4[0][116-45:122-45].set_color(YELLOW)
        sc_4[0][132-45:145-45].set_color(YELLOW)
        sc_4[0][80+27:102+27].set_color(YELLOW)

        self.play(FadeIn(sc_4))
        self.next_slide()

        sc_5 = MyTex(r'''
        PSD cone $\cc{S}^n_+$:
        \begin{myitemize}
        \item[] Space: $\bJ = \bR^{n^2}$ \hspace{2em}
        Jordan product: $\mmx \circ\mmy = {1\over 2} \vecc(\mmX\mmY + \mmY\mmX)$\\
        \vspace{-1.3em}
        \item[] Identity: $\mme = \vecc(\mmI)$ \hspace{1em}
        Trace: $\Tr(\mmx) = \Tr(\mmX)$ \hspace{1em}
        Inner product: $\mmx \bullet \mmy = \mmx^T \mmy$\\
        \vspace{-1.3em}
        \item[] Spectral decomposition: $\eigenval{k}{\mmx} = \eigenval{k}{\mmX},\ \mmq_k = \vecc(\mmv_k\mmv_k^T)$\\
        \end{myitemize}
        ''', up=sc_4)
        sc_5[0][:11].set_color(BLUE)
        sc_5[0][11:17].set_color(YELLOW)
        sc_5[0][22:36].set_color(YELLOW)
        sc_5[0][53:62].set_color(YELLOW)
        sc_5[0][117-47:123-47].set_color(YELLOW)
        sc_5[0][134-47:147-47].set_color(YELLOW)
        sc_5[0][70+37:92+37].set_color(YELLOW)

        self.play(FadeIn(sc_5))
        self.next_slide()

        self.play(FadeOut(sc_4, sc_5))

        sc_6 = MyTex(r'''
        Second-order cone $\cc{Q}^{d+1}$: $\quad \mmx = (\bar{\mmx}, x_0),\ \mmy = (\bar{\mmy}, y_0)$
        \begin{myitemize}
        \item[] Space: $\bJ = \bR^{d}\times \bR$ \hspace{2em}
        Jordan product: $\mmx \circ \mmy = {1\over \sqrt{2}}(x_0\bar{\mmy} + y_0\bar{\mmx},\ \mmx^T \mmy)$\\
        \vspace{-1.3em}
        \item[] Identity: $\mme = (\mmzero, \sqrt{2})$ \hspace{1em}
        Trace: $\Tr(\mmx) = \sqrt{2} x_0$ \hspace{1em}
        Inner product: $\mmx \bullet \mmy = \mmx^T \mmy$\\
        \vspace{-1.3em}
        \item[] Spectral decomposition: $\eigenval{1,2}{\mmx} = {1\over\sqrt{2}} (x_0 \pm \|\bar{\mmx}\|),\ \mmq_{1,2} = {1\over \sqrt{2}} (\pm \mmu, 1)$\\
        \end{myitemize}
        ''', up=subtitle_eja)
        sc_6[0][:21].set_color(BLUE)
        sc_6[0][11+29:17+29].set_color(YELLOW)
        sc_6[0][22+30:36+30].set_color(YELLOW)
        sc_6[0][53+37:62+37].set_color(YELLOW)
        sc_6[0][117-9:123-9].set_color(YELLOW)
        sc_6[0][134-9:147-9].set_color(YELLOW)
        sc_6[0][70+75:92+75].set_color(YELLOW)

        self.play(FadeIn(sc_6))
        self.next_slide()

        sc_7 = MyTex(r'''
        Product cone $\cc{K}_1\times \dots \times \cc{K}_n$: $\quad \mmx = \cproduct_{i=1}^n \mmx_i = (\mmx_1, \dots, \mmx_n)$
        \begin{myitemize}
        \item[] Space: $\bJ = \bJ_1 \times \dots \times \bJ_n$ \hspace{2em}
        Jordan product: $\mmx \circ \mmy = \cproduct_{i=1}^n (\mmx_i \circ \mmy_i)$\\
        \vspace{-1.3em}
        \item[] Identity, trace, inner product: concatenation/sum of those of sub-EJAs\\
        \vspace{-1.3em}
        \item[] Spectral decomposition: follows from the decompositions of sub-EJAs\\
        \end{myitemize}
        ''', up=sc_6)
        sc_7[0][:21].set_color(BLUE)
        sc_7[0][11+31:17+31].set_color(YELLOW)
        sc_7[0][22+37:36+37].set_color(YELLOW)
        sc_7[0][53+36:62+55].set_color(YELLOW)
        sc_7[0][70+81:92+81].set_color(YELLOW)

        self.play(FadeIn(sc_7))
        self.next_slide()
        
        self.play(FadeOut(sc_6, sc_7))




###########################################################################################################################
###########################################################################################################################
###########################################################################################################################
# # Zero-Sum Game #########################################################################################################

        self.play(subtitle_eja.animate.move_to(outline_pos['subtitle_eja']),
            FadeIn(outline_title, subtitle_game, subtitle_geometry, subtitle_scp, subtitle_parallel, subtitle_conclu)
        )
        self.next_slide()
        self.play(subtitle_game.animate.to_edge(UL, buff=0.5),
            FadeOut(outline_title, subtitle_eja, subtitle_geometry, subtitle_scp, subtitle_parallel, subtitle_conclu)
        )
        self.next_slide()

        game_circle_2 = Circle(radius=0.8, fill_color=RED, fill_opacity=0.2).stretch_to_fit_height(3.5).rotate(-PI/5).stretch_to_fit_height(3.5).shift(UP * 0.5)
        game_circle_1 = Circle(radius=1.3, fill_color=RED, fill_opacity=0.2).stretch_to_fit_height(3.5).next_to(game_circle_2, LEFT, buff=1.5)
        game_polygon = Polygon([0, 0, 0], [-1, 2, 0], [1, 4, 0], [5, 4, 0], [4, 0.5, 0], color=YELLOW, fill_color=YELLOW, fill_opacity=0.2).scale(0.5).stretch_to_fit_height(3.5).next_to(game_circle_2, RIGHT, buff=1.5)

        game_alice = Text("Alice", color=RED).scale(0.6).next_to(game_circle_1, UP)
        game_bob = Text("Bob", color=YELLOW).scale(0.6).next_to(game_polygon, UP)

        game_circle_1_text = MyTex(r'$\cc{A}\subseteq \bU$').set_color(RED).scale(0.8).move_to(game_circle_1.get_center())
        game_circle_2_text = MyTex(r'$\brmf(\cc{A})\subseteq \bJ$').set_color(RED).scale(0.8).move_to(game_circle_2.get_center())
        game_polygon_text = MyTex(r'\[\begin{gathered}\cc{B}=\big\{\mmy \in \cc{K}: \Tr(\mmy) = 1 \big\}\\ \subseteq \bJ \end{gathered}\]').set_color(YELLOW).scale(0.8).rotate(PI/3).move_to(game_polygon.get_center())

        self.play(FadeIn(game_circle_1, game_polygon, game_alice, game_bob, game_circle_1_text, game_polygon_text))

        self.next_slide()

        alice_point = Dot(game_circle_1.get_center(), radius=0.05, color=WHITE).shift(RIGHT * 0.5 + UP * 1)
        alice_point_label = MyTex(r'$\mmx$').next_to(alice_point, UL, buff=0.05)
        bob_point = Dot(game_polygon.get_center(), radius=0.05, color=WHITE).shift(LEFT * 0.6 + UP * 0.7)
        bob_point_label = MyTex(r'$\mmy$').next_to(bob_point, UR, buff=0.05)
        
        self.play(FadeIn(alice_point, alice_point_label, bob_point, bob_point_label))

        self.next_slide()
        
        alice_point_2 = Dot(game_circle_2.get_center(), radius=0.05, color=WHITE).shift(RIGHT * 0.5 + UP * 1)
        alice_point_2_label = MyTex(r'$\brmf(\mmx)$').next_to(alice_point_2, DOWN, buff=0.1)
        alice_trans_arrow = Arrow(alice_point, alice_point_2, buff=0.1, stroke_width=4, max_tip_length_to_length_ratio=0.05)
        alice_trans_text = MyTex(r'$\brmf : \bU \rightarrow \bJ$').scale(0.9).rotate(-PI/120).next_to(alice_trans_arrow, UP, buff=0.1)
        
        self.play(FadeIn(game_circle_2, game_circle_2_text))
        self.play(AnimationGroup(Create(alice_trans_arrow), Create(alice_trans_text), lag_ratio=0.5))
        self.play(FadeIn(alice_point_2, alice_point_2_label))

        self.next_slide()

        alice_bob_seg = Line(alice_point_2, bob_point, buff=0.1)
        alice_bob_arrow = Arrow(alice_bob_seg.get_center(), alice_bob_seg.get_center() + DOWN * 2.8, buff=0, max_tip_length_to_length_ratio=0.07)
        alice_bob_payoff = MyTex(r'$\brmf(\mmx) \bullet \mmy$').next_to(alice_bob_arrow, DOWN, buff=0.2).set_color(BLUE)
        alice_bob_minmax = MyTex(r'$\displaystyle\max_{\mmx\in \cc{A}} \min_{\mmy\in \cc{B}}$').next_to(alice_bob_payoff, LEFT, buff=0.1).set_color(BLUE).shift(DOWN * 0.1)

        game_setting = Group(alice_bob_payoff, alice_bob_minmax)

        self.play(AnimationGroup(Create(alice_bob_seg), Create(alice_bob_arrow), Create(alice_bob_payoff), lag_ratio=0.5))
        
        self.next_slide()

        self.play(FadeIn(alice_bob_minmax))

        self.next_slide()

        self.play(AnimationGroup(
            FadeOut(game_circle_1, game_circle_2, game_polygon, game_circle_1_text, game_circle_2_text, game_polygon_text, 
            game_alice, game_bob, alice_point, bob_point, alice_point_2, alice_point_label, bob_point_label, alice_point_2_label, 
            alice_bob_arrow, alice_bob_seg, alice_trans_arrow, alice_trans_text),
            game_setting.animate.move_to([-1,0,0]).scale(1.3).set_color(WHITE),
            lag_ratio = 0.5
        ))

        self.next_slide()

        minimax_theorem_text = MyTex(r'Minimax theorem:').scale(1.3).set_color(BLUE).next_to(game_setting, LEFT, buff=0.2).shift(UP * 0.15)
        minimax_theorem_eq = MyTex(r'$= \displaystyle\min_{\mmy\in\cc{B}} \displaystyle\max_{\mmx\in\cc{A}}\ \brmf(\mmx)\bullet \mmy = \lambda^*$').scale(1.3).next_to(game_setting, RIGHT, buff=0.15)
        minimax_theorem_group = Group(game_setting, minimax_theorem_text, minimax_theorem_eq)

        self.play(Create(minimax_theorem_text))
        self.play(Create(minimax_theorem_eq))
        self.wait()
        self.next_slide()

        self.play(minimax_theorem_group.animate.scale(1/1.3).next_to(subtitle_game, DOWN, buff=0.5).to_edge(LEFT, buff=1))

        self.next_slide()

        nash_equilibrium = MyTex(r'''
        $\eps$-Nash equilibrium: find $\tilde{\mmx}\in \cc{A}$ and $\tilde{\mmy}\in\cc{B}$ such that
        \[
        \begin{aligned}
            \min_{\mmy\in \cc{B}}\ \brmf(\tilde{\mmx})\bullet \mmy & \ge \lambda^* - \eps, \\
            \max_{\mmx\in \cc{A}}\ \brmf(\mmx)\bullet \tilde{\mmy} & \le \lambda^* + \eps.
        \end{aligned}
        \]
        ''', up=minimax_theorem_group)
        nash_equilibrium[0][:18].set_color(YELLOW)
        nash_equilibrium[0][21:25].set_color(RED)
        nash_equilibrium[0][28:32].set_color(RED)
        nash_equilibrium[0][48:50].set_color(RED)
        nash_equilibrium[0][70:72].set_color(RED)

        self.play(FadeIn(nash_equilibrium))

        self.next_slide()

        oracle_intro = MyTex(r'''
        The {\sc Oracle}: given any $\mmy \in \cc{B}$, provides the best response $\mmx \in \cc{A}$ such that
        \[
            \mmx = \argmax_{\mmx \in \cc{A}}\ \brmf(\mmx) \bullet \mmy
        \]
        ''', up=nash_equilibrium)
        oracle_intro[0][:10].set_color(YELLOW)

        self.play(FadeIn(oracle_intro))
        self.next_slide()

        oracle_width_intro = MyTex(r'''
        Width $\rho$ of {\sc Oracle}: an upper bound on $\|\brmf(\mmx)\|_\infty$, namely $\|\brmf(\mmx)\|_\infty \le \rho$
        ''', up=oracle_intro)
        oracle_width_intro[0][:15].set_color(YELLOW)

        self.play(FadeIn(oracle_width_intro))
        self.next_slide()

        self.play(FadeOut(minimax_theorem_group, oracle_intro, nash_equilibrium, oracle_width_intro))

        game_thm = Theorem(r'''
        {\bf\underline{Thm:}} An $\eps$-Nash equilibrium can be found using $O(\rho^2 \log r / \eps^2)$ {\sc Oracle} calls
        ''')

        self.play(FadeIn(game_thm))
        self.next_slide()
        
        self.play(game_thm.animate.scale(0.5).to_edge(UR, buff=0.5))

        self.next_slide()

        game_bob.set_color(WHITE).next_to(subtitle_game, DOWN, buff=0.5).to_edge(LEFT, buff=2)
        game_alice = Group(game_alice.set_color(WHITE), MyTex(r'({\sc Oracle})').next_to(game_alice, RIGHT, buff=0.1)).next_to(game_bob, RIGHT, buff=3.5)
        game_payoff = Text("Payoff", color=WHITE).scale(0.6).next_to(game_alice, RIGHT, buff=2)

        bob_round = [MyTex(r'$\xt{\mmy}{1} = {\mme \over r}$').next_to(game_bob, DOWN, buff=0.5)]
        alice_round = [MyTex(r'$\xt{\mmx}{1} = \displaystyle\argmax_{\mmx\in\cc{A}} \brmf(\mmx) \bullet \xt{\mmy}{1}$').next_to(game_alice, DOWN, buff=0.5)]
        alice_round[-1].shift([0, bob_round[-1].get_center()[1] - alice_round[-1].get_center()[1] - 0.1, 0])
        payoff_round = [MyTex(r'$\brmf(\xt{\mmx}{1}) \bullet \xt{\mmy}{1}$').next_to(game_payoff, DOWN, buff=0.5)]
        payoff_round[-1].shift([0, bob_round[-1].get_center()[1] - payoff_round[-1].get_center()[1], 0])

        bob_round.append(MyTex(r'$\xt{\mmy}{2} = {\mmexp\big(-{\eta\over \rho}\brmf(\xt{\mmx}{1})\big) \over \Tr\Big(\mmexp\big(-{\eta\over \rho}\brmf(\xt{\mmx}{1})\big)\Big)}$').next_to(bob_round[-1], DOWN, buff=0.25))
        alice_round.append(MyTex(r'$\xt{\mmx}{2} = \displaystyle\argmax_{\mmx\in\cc{A}} \brmf(\mmx) \bullet \xt{\mmy}{2}$').next_to(alice_round[-1], DOWN, buff=0.25))
        alice_round[-1].shift([0, bob_round[-1].get_center()[1] - alice_round[-1].get_center()[1] - 0.1, 0])
        payoff_round.append(MyTex(r'$\brmf(\xt{\mmx}{2}) \bullet \xt{\mmy}{2}$').next_to(payoff_round[-1], DOWN, buff=0.25))
        payoff_round[-1].shift([0, bob_round[-1].get_center()[1] - payoff_round[-1].get_center()[1], 0])

        bob_round.append(MyTex(r'$\xt{\mmy}{3} = {\mmexp\big(-{\eta\over \rho}\sum_{\tau=1}^{2}\brmf(\xt{\mmx}{\tau})\big) \over \Tr\Big(\mmexp\big(-{\eta\over \rho}\sum_{\tau=1}^{2}\brmf(\xt{\mmx}{\tau})\big)\Big)}$').next_to(bob_round[-1], DOWN, buff=0.25))
        alice_round.append(MyTex(r'$\xt{\mmx}{3} = \displaystyle\argmax_{\mmx\in\cc{A}} \brmf(\mmx) \bullet \xt{\mmy}{3}$').next_to(alice_round[-1], DOWN, buff=0.25))
        alice_round[-1].shift([0, bob_round[-1].get_center()[1] - alice_round[-1].get_center()[1] - 0.1, 0])
        payoff_round.append(MyTex(r'$\brmf(\xt{\mmx}{3}) \bullet \xt{\mmy}{3}$').next_to(payoff_round[-1], DOWN, buff=0.25))
        payoff_round[-1].shift([0, bob_round[-1].get_center()[1] - payoff_round[-1].get_center()[1], 0])

        vdots = [MyTex(r'$\vdots$') for i in range(3)]
        vdots[0].next_to(bob_round[-1], DOWN, buff=0.5)
        vdots[1].next_to(alice_round[-1], DOWN, buff=0.5).shift([0,vdots[0].get_center()[1] - vdots[1].get_center()[1],0])
        vdots[2].next_to(payoff_round[-1], DOWN, buff=0.5).shift([0,vdots[0].get_center()[1] - vdots[2].get_center()[1],0])

        bob_round.append(MyTex(r'$\xt{\mmy}{T} = {\mmexp\big(-{\eta\over \rho}\sum_{\tau=1}^{T-1}\brmf(\xt{\mmx}{\tau})\big) \over \Tr\Big(\mmexp\big(-{\eta\over \rho}\sum_{\tau=1}^{T-1}\brmf(\xt{\mmx}{\tau})\big)\Big)}$').next_to(vdots[0], DOWN, buff=0.5))
        alice_round.append(MyTex(r'$\xt{\mmx}{T} = \displaystyle\argmax_{\mmx\in\cc{A}} \brmf(\mmx) \bullet \xt{\mmy}{T}$').next_to(vdots[1], DOWN, buff=0.5))
        alice_round[-1].shift([0, bob_round[-1].get_center()[1] - alice_round[-1].get_center()[1] - 0.1, 0])
        payoff_round.append(MyTex(r'$\brmf(\xt{\mmx}{T}) \bullet \xt{\mmy}{T}$').next_to(vdots[2], DOWN, buff=0.5))
        payoff_round[-1].shift([0, bob_round[-1].get_center()[1] - payoff_round[-1].get_center()[1], 0])

        game_avg_line = Line(bob_round[-1].get_left(), payoff_round[-1].get_right() + [0.5,0,0])
        game_avg_line.shift([0, bob_round[-1].get_bottom()[1] - game_avg_line.get_center()[1] - 0.2, 0])

        game_avg = []
        game_avg.append(MyTex(r'$\tilde{\mmy} = {1\over T} \sum_{t=1}^T \xt{\mmy}{t}$').set_color(BLUE).next_to(bob_round[-1], DOWN, buff=0.2))
        game_avg.append(MyTex(r'$\tilde{\mmx} = {1\over T} \sum_{t=1}^T \xt{\mmx}{t}$').set_color(BLUE).next_to(alice_round[-1], DOWN, buff=0.2))
        game_avg.append(MyTex(r'${1\over T}\sum_{t=1}^T \brmf(\xt{\mmx}{t}) \bullet \xt{\mmy}{t}$').set_color(BLUE).next_to(payoff_round[-1], DOWN, buff=0.2))
        for avg in game_avg:
            avg.shift([0, game_avg_line.get_bottom()[1] - avg.get_top()[1] - 0.2, 0])

        game_process_group = Group(game_bob, game_alice, game_payoff, *bob_round, *alice_round, *payoff_round, *vdots, game_avg_line, *game_avg)
        game_process_group.scale(0.9, about_point=game_process_group.get_top())
        game_process_group.shift([-game_process_group.get_center()[0], 0, 0])

        self.play(FadeIn(game_alice, game_bob, game_payoff))
        self.next_slide()
        self.play(FadeIn(bob_round[0]))
        self.next_slide()
        self.play(FadeIn(alice_round[0]))
        self.next_slide()
        self.play(FadeIn(payoff_round[0]))
        self.next_slide()
        self.play(FadeIn(bob_round[1]))
        self.next_slide()
        self.play(FadeIn(alice_round[1]))
        self.next_slide()
        self.play(FadeIn(payoff_round[1]))
        self.next_slide()
        self.play(FadeIn(bob_round[2]))
        self.wait()
        self.next_slide()
        self.play(FadeIn(alice_round[2]))
        self.next_slide()
        self.play(FadeIn(payoff_round[2]))
        self.next_slide()
        self.play(FadeIn(*vdots, bob_round[-1], alice_round[-1], payoff_round[-1]))
        self.next_slide()
        self.play(Create(game_avg_line))
        self.play(FadeIn(*game_avg))
        self.wait()
        self.next_slide()

        self.play(game_process_group.animate.scale(0.7, about_point=game_process_group.get_top()))
        self.next_slide()

        game_claim = Theorem(r'''
        {\bf\underline{Claim:}}
        Choose $T = \lceil{4\rho^2 \ln r \over \eps^2}\rceil$ and $\eta = \sqrt{ {\ln r \over T} }$, we have:

        $\lambda^*\ \overset{(i)}{\le}\ \displaystyle\max_{\mmx\in\cc{A}}\ \brmf(\mmx)\bullet\tilde{\mmy}\ \overset{(ii)}{\le}\ {1\over T}\sum_{t=1}^T \brmf(\xt{\mmx}{t}) \bullet \xt{\mmy}{t} \ \overset{(iii)}{\le}\ \displaystyle\min_{\mmy\in\cc{B}}\ \brmf(\tilde{\mmx})\bullet \mmy + \eps\ \overset{(iv)}{\le}\ \lambda^* + \eps$
        ''', edge_color=BLUE).scale(0.8).next_to(game_process_group, DOWN, buff=0.3)
        
        self.play(FadeIn(game_claim))
        self.next_slide()

        self.play(FadeOut(game_process_group), game_claim.animate.scale(0.5/0.8).next_to(game_thm, DOWN, buff=0.1).to_edge(RIGHT, buff=0.5))

        self.wait()
        self.next_slide()

        game_proof = []

        game_proof.append([
        MyTex(r'''
        \[ (i)\ \max_{\mmx\in\cc{A}}\ \brmf(\mmx)\bullet \tilde{\mmy}
            \ge \min_{\mmy\in\cc{B}} \max_{\mmx\in\cc{A}}\ \brmf(\mmx)\bullet \mmy
            = \lambda^* \]
        '''),
        MyTex(r'''
        \[ (i)\ \max_{\mmx\in\cc{A}}\ \brmf(\mmx)\bullet \tilde{\mmy}
            \ge \lambda^* \]
        ''').scale(0.8).next_to(subtitle_game, DOWN, buff=0.5).to_edge(LEFT, buff=1).set_color(BLUE)
        ])

        game_proof.append([
        MyTex(r'''
        \[ (iv)\ \min_{\mmy\in\cc{B}}\ \brmf(\tilde{\mmx}) \bullet \mmy
            \le \max_{\mmx\in\cc{A}} \min_{\mmy\in\cc{B}}\ \brmf(\mmx)\bullet \mmy
            = \lambda^* \]
        '''),
        MyTex(r'''
        \[ (iv)\ \min_{\mmy\in\cc{B}}\ \brmf(\tilde{\mmx}) \bullet \mmy + \eps
            \le \lambda^* + \eps \]
        ''').scale(0.8).next_to(game_proof[-1][-1], DOWN, buff=0.25).to_edge(LEFT, buff=1).set_color(BLUE)
        ])

        game_proof.append([
        MyTex(r'''
        \[ (ii)\ \brmf(\mmx^*)\bullet\xt{\mmy}{t} \le \max_{\mmx \in \cc{A}}\ \brmf(\mmx) \bullet \xt{\mmy}{t} \]
        '''),
        MyTex(r'''
        \[ (ii)\ \brmf(\mmx^*)\bullet\xt{\mmy}{t} \le \brmf(\xt{\mmx}{t}) \bullet \xt{\mmy}{t} \]
        '''),
        MyTex(r'''
        \[ (ii)\ {1\over T} \sum_{t=1}^T \brmf(\mmx^*)\bullet\xt{\mmy}{t} \le {1\over T}\sum_{t=1}^T \brmf(\xt{\mmx}{t}) \bullet \xt{\mmy}{t} \]
        '''),
        MyTex(r'''
        \[ (ii)\ \brmf(\mmx^*)\bullet\tilde{\mmy} \le {1\over T}\sum_{t=1}^T \brmf(\xt{\mmx}{t}) \bullet \xt{\mmy}{t} \]
        '''),
        MyTex(r'''
        \[ (ii)\ \max_{\mmx\in\cc{A}}\ \brmf(\mmx)\bullet\tilde{\mmy} \le {1\over T}\sum_{t=1}^T \brmf(\xt{\mmx}{t}) \bullet \xt{\mmy}{t} \]
        ''')
        ])

        self.play(FadeIn(game_proof[0][0]))
        self.wait()
        self.next_slide()
        self.play(ReplacementTransform(game_proof[0][0], game_proof[0][1]))

        self.play(FadeIn(game_proof[1][0]))
        self.wait()
        self.next_slide()
        self.play(ReplacementTransform(game_proof[1][0], game_proof[1][1]))

        self.play(FadeIn(game_proof[2][0]))
        self.wait()
        self.next_slide()
        self.play(ReplacementTransform(game_proof[2][0], game_proof[2][1]))
        self.wait()
        self.next_slide()
        self.play(ReplacementTransform(game_proof[2][1], game_proof[2][2]))
        self.wait()
        self.next_slide()
        self.play(ReplacementTransform(game_proof[2][2], game_proof[2][3]))
        self.wait()
        self.next_slide()
        self.play(ReplacementTransform(game_proof[2][3], game_proof[2][4]))
        self.wait()
        self.next_slide()
        self.play(game_proof[2][4].animate.scale(0.8).next_to(game_proof[1][-1], DOWN, buff=0).to_edge(LEFT, buff=1).set_color(BLUE))
        self.wait()
        self.next_slide()

        game_eigenval_claim = Theorem(r'''
        {\bf\underline{Claim:}} $\displaystyle {1\over T}\sum_{t=1}^T \brmf(\xt{\mmx}{t}) \bullet \xt{\mmy}{t} \le \lambda_{\min}\Big({1\over T}\sum_{t=1}^T \brmf(\xt{\mmx}{t})\Big) + \eps \le \min_{\mmy\in\cc{B}}\ \brmf(\tilde{\mmx})\bullet \mmy + \eps$
        ''', edge_color=GREEN).shift(DOWN * 0.5)
        
        self.play(FadeIn(game_eigenval_claim))
        self.wait()
        self.next_slide()

        self.play(game_eigenval_claim.animate.scale(0.5).next_to(game_claim, DOWN, buff=0.1).to_edge(RIGHT, buff=0.5), FadeOut(game_proof[0][1]), FadeOut(game_proof[1][1]), FadeOut(game_proof[2][4]))

        self.next_slide()

        game_eigenval_proof = []
        game_eigenval_proof.append(
            Text('Proof sketch:', color=GREEN).scale(0.5).next_to(subtitle_game, DOWN, buff=1).to_edge(LEFT, buff=1)
        )
        game_eigenval_proof.append(
            MyTex(r'''\scalebox{0.8}{
            $ \xt{\mmw}{1} = \mme,\ \xt{\mmw}{t} = \displaystyle\mmexp\Big(-{\eta\over \rho}\sum_{\tau=1}^{t-1}\brmf(\xt{\mmx}{\tau})\Big) $
            } ''', up=game_eigenval_proof[-1], buff=0.25)
        )
        game_eigenval_proof.append(
            MyTex(r'''\scalebox{0.8}{
            Upper bound: $\displaystyle \Tr(\xt{\mmw}{T+1}) \le \Tr(\xt{\mmw}{T})\cdot\exp\Big(- {\eta\over \rho}\brmf(\xt{\mmx}{T})\bullet\xt{\mmy}{T} + {\eta^2\over \rho^2}\big(\brmf(\xt{\mmx}{T})\big)^2\bullet\xt{\mmy}{T}\Big)$
            } ''', up=game_eigenval_proof[-1], buff=0.25)
        )
        game_eigenval_proof.append(
            MyTex(r'''\scalebox{0.8}{
            Upper bound: $\displaystyle \Tr(\xt{\mmw}{T+1}) \le r\cdot\exp\Big(-\sum_{t=1}^T {\eta\over \rho} \brmf(\xt{\mmx}{t})\bullet \xt{\mmy}{t} + \sum_{t=1}^T {\eta^2\over \rho^2}\big(\brmf(\xt{\mmx}{t})\big)^2\bullet\xt{\mmy}{t}\Big)$
            } ''', up=game_eigenval_proof[-2], buff=0.24)
        )
        game_eigenval_proof.append(
            MyTex(r'''\scalebox{0.8}{
            Lower bound: $\displaystyle \Tr(\xt{\mmw}{T+1}) \ge \displaystyle\exp\Big(-{\eta\over \rho}\lambda_{\min}\big(\sum_{t=1}^{T}\brmf(\xt{\mmx}{t})\big)\Big)$
            } ''', up=game_eigenval_proof[-1], buff=0.25)
        )

        self.play(FadeIn(game_eigenval_proof[0]))
        self.wait()
        self.next_slide()

        self.play(FadeIn(game_eigenval_proof[1]))
        self.wait()
        self.next_slide()

        self.play(FadeIn(game_eigenval_proof[2]))
        self.wait()
        self.next_slide()

        self.play(ReplacementTransform(game_eigenval_proof[2], game_eigenval_proof[3]))
        self.wait()
        self.next_slide()

        self.play(FadeIn(game_eigenval_proof[4]))
        self.wait()
        self.next_slide()

        game_eigenval_proof.append([])
        game_eigenval_proof[-1].append(
            MyTex(r'''\scalebox{0.8}{
            $\displaystyle r\cdot\exp\Big(-\sum_{t=1}^T {\eta\over \rho} \brmf(\xt{\mmx}{t})\bullet \xt{\mmy}{t} + \sum_{t=1}^T {\eta^2\over \rho^2}\big(\brmf(\xt{\mmx}{t})\big)^2\bullet\xt{\mmy}{t}\Big) \ge \exp\Big(-{\eta\over \rho}\lambda_{\min}\big(\sum_{t=1}^{T}\brmf(\xt{\mmx}{t})\big)\Big) $
            } ''', up=game_eigenval_proof[-2], buff=0.25)
        )
        game_eigenval_proof[-1].append(
            MyTex(r'''\scalebox{0.8}{
            $\displaystyle {\rho\ln(r)\over \eta T} -{1\over T} \sum_{t=1}^T \brmf(\xt{\mmx}{t}) \bullet \xt{\mmy}{t} + \eta \rho \ge -{1\over T}\lambda_{\min}\big(\sum_{t=1}^{T}\brmf(\xt{\mmx}{t})\big) = -\lambda_{\min}\big(\brmf(\tilde{\mmx})\big)$
            } ''', up=game_eigenval_proof[-2], buff=0.25)
        )
        game_eigenval_proof[-1].append(
            MyTex(r'''\scalebox{0.8}{
            $\displaystyle \eps -{1\over T} \sum_{t=1}^T \brmf(\xt{\mmx}{t}) \bullet \xt{\mmy}{t} \ge -\lambda_{\min}\big(\brmf(\tilde{\mmx})\big)$
            } ''', up=game_eigenval_proof[-2], buff=0.25)
        )

        self.play(FadeIn(game_eigenval_proof[-1][0]))
        self.next_slide()
        self.play(ReplacementTransform(game_eigenval_proof[-1][0], game_eigenval_proof[-1][1]))
        self.wait()
        self.next_slide()
        self.play(ReplacementTransform(game_eigenval_proof[-1][1], game_eigenval_proof[-1][2]))
        self.wait()
        self.next_slide()

        game_eigenval_proof.append(
            MyTex(r'''\scalebox{0.9}{
            $ \big|{\eta \over \rho}\brmf(\xt{\mmx}{t})\bullet \xt{\mmy}{t}\big| \le 1 \ \Leftarrow \ \|{\eta \over \rho}\brmf(\xt{\mmx}{t})\|_\infty \le 1 \ \Leftarrow \ \|\brmf(\xt{\mmx}{t})\|_\infty \le \rho $
            } ''').next_to(game_eigenval_proof[-1][-1], DOWN, buff=0.5).to_edge(LEFT, buff=1).set_color(RED)
        )

        self.play(Create(game_eigenval_proof[-1]))
        self.wait()
        self.next_slide()

        self.play(FadeOut(game_thm, game_claim, game_eigenval_claim, game_eigenval_proof[0], game_eigenval_proof[1], game_eigenval_proof[3], game_eigenval_proof[4], game_eigenval_proof[5][2], game_eigenval_proof[-1]))






########################################################################################################################
########################################################################################################################
########################################################################################################################
# Geometric Optimization ###############################################################################################

        self.play(subtitle_game.animate.move_to(outline_pos['subtitle_game']),
            FadeIn(outline_title, subtitle_eja, subtitle_geometry, subtitle_scp, subtitle_parallel, subtitle_conclu)
        )
        self.next_slide()
        self.play(subtitle_geometry.animate.to_edge(UL, buff=0.5).set_color(WHITE),
            FadeOut(outline_title, subtitle_eja, subtitle_game, subtitle_scp, subtitle_parallel, subtitle_conclu)
        )
        self.next_slide()

        geometry_summary_table = GeometrySummary()
        geometry_summary_notes = MyTex(r'''\scalebox{0.9}{
        $d$: dimensions, \hspace{.5em}
        $n$: number of objs, \hspace{.5em}
        $M$: number of pts, \hspace{.5em}
        $N$: number of nonzeros
        } ''').next_to(geometry_summary_table, DOWN, buff=0.2)

        self.play(FadeIn(geometry_summary_table, geometry_summary_notes))
        self.wait()
        self.next_slide()

        self.play(FadeOut(geometry_summary_table, geometry_summary_notes))

        geoemtry_subtitle_sib = Text(": SIB").set_font_size(25).next_to(subtitle_geometry, RIGHT, buff=0.1).shift(UP * 0.02)

        self.play(Create(geoemtry_subtitle_sib))
        self.wait()
        self.next_slide()

        geometry_draw_sib = Circle(radius=sib.radius, color=RED, fill_opacity=0.3)
        geometry_draw_sib_labels = []
        for i in range(len(sib.objects)):
            geometry_draw_sib_labels.append(
                MyTex(f'$\Omega_{i + 1}$').move_to(sib.objects[i].get_center())
            )
        geometry_draw_sib_group = Group(geometry_draw_sib, *sib.objects, *geometry_draw_sib_labels)

        self.play(FadeIn(*sib.objects, *geometry_draw_sib_labels))
        self.wait()
        self.next_slide()

        self.play(Create(geometry_draw_sib))
        self.wait()
        self.next_slide()

        geometry_sib_problem = [
            MyTex(r'Smallest intersecting ball', up=subtitle_geometry).set_color(BLUE),
            MyTex(r'''
                \[
                \begin{aligned}
                    \underset{\mmz, \mmv_1, \dots, \mmv_n, r}{\rm minimize} \quad& r\\
                    {\rm subject\ to} \quad& \|\mmz - \mmv_i\| \le r, \ \forall i \in [n],\\
                    & \mmv_i \in \Omega_i,\ \forall i \in [n].
                \end{aligned}
                \]
            '''),
            MyTex(r'''
                \[
                \begin{aligned}
                    \underset{\mmz, \mmv_1, \dots, \mmv_n, r}{\rm minimize} \quad& r\\
                    {\rm subject\ to} \quad& \begin{pmatrix}\mmz - \mmv_i \\ r\end{pmatrix} \in \cc{Q}^{d+1}, \ \forall i \in [n],\\
                    & \mmv_i \in \Omega_i,\ \forall i \in [n].
                \end{aligned}
                \]
            '''),
            MyTex(r'''
                \[
                \begin{aligned}
                    \underset{\mmz, \mmv_1, \dots, \mmv_n, r}{\rm minimize} \quad& r\\
                    {\rm subject\ to} \quad& \cproduct_{i=1}^n \begin{pmatrix}\mmz - \mmv_i \\ r\end{pmatrix} \in \cproduct_{i=1}^n \cc{Q}^{d+1},\\
                    & \mmv_i \in \Omega_i,\ \forall i \in [n].
                \end{aligned}
                \]
            ''')
        ]
        for i in range(1, len(geometry_sib_problem)):
            geometry_sib_problem[i].next_to(geometry_sib_problem[0], DOWN, buff=0.25).shift([geometry_sib_problem[0].get_left()[0] - geometry_sib_problem[i].get_left()[0], 0, 0])
        geometry_sib_problem_group = Group(*geometry_sib_problem[:2])

        self.play(FadeIn(*geometry_sib_problem[:2]),
            geometry_draw_sib_group.animate.scale(0.5).next_to(geometry_sib_problem_group, RIGHT, buff=1)
        )
        self.wait()
        self.next_slide()

        geometry_sib_claim = Theorem(r'''
        {\bf\underline{Claim:}} Any solution to SIB satisfies $\mmz \in \conv(\{\Omega_i\}_{i=1}^n)$.
        ''', edge_color=BLUE).next_to(geometry_sib_problem_group, DOWN, buff=1)
        geometry_sib_claim.shift([-geometry_sib_claim.get_center()[0], 0, 0])
        
        self.play(FadeIn(geometry_sib_claim))
        self.wait()
        self.next_slide()

        self.play(geometry_sib_claim.animate.scale(0.5).to_edge(UR, buff=0.5), FadeOut(geometry_draw_sib_group))
        self.wait()
        self.next_slide()

        self.play(FadeIn(geometry_sib_problem[2]), FadeOut(geometry_sib_problem[1]))
        self.wait()
        self.next_slide()

        self.play(FadeIn(geometry_sib_problem[3]), FadeOut(geometry_sib_problem[2]))
        self.wait()
        self.next_slide()

        geometry_sib_ftp_question = [
            MyTex(r'Question: Let $r^*$ be the optimal radius. Given $\hat{r}$, is $\hat{r} \ge r^*$ or $\hat{r} < r^*$?', up=geometry_sib_problem[3]),
            MyTex(r'Question: Given $\hat{r}$ and $\eps > 0$, is $(1 + \eps) \hat{r} \ge r^*$ or $\hat{r} < r^*$?', up=geometry_sib_problem[3]),
            MyTex(r'Feasibility test problem (FTP)', up=geometry_sib_problem[3])
        ]
        geometry_sib_ftp_question[0][0][:9].set_color(YELLOW)
        geometry_sib_ftp_question[1][0][:9].set_color(YELLOW)
        geometry_sib_ftp_question[2][0].set_color(YELLOW)

        self.play(Create(geometry_sib_ftp_question[0]))
        self.wait()
        self.next_slide()

        geometry_sib_ftp = [
            MyTex(r'''
            Find $\mmz, \mmv_1, \dots, \mmv_n, r$ such that
            ''', up=geometry_sib_ftp_question[0], buff=0.25),
            MyTex(r'''
                \[
                \begin{aligned}
                    & r \le \hat{r},\\
                    & \cproduct_{i=1}^n \begin{pmatrix}\mmz - \mmv_i \\ r\end{pmatrix} \in \cproduct_{i=1}^n \cc{Q}^{d+1},\\
                    & \mmv_i \in \Omega_i,\ \forall i \in [n],\\
                    & \mmz \in \conv(\{\Omega_i\}_{i=1}^n).
                \end{aligned}
                \]
            '''),
            MyTex(r'''
                \[
                \begin{aligned}
                    & r \le (1 + \eps)\hat{r},\\
                    & \cproduct_{i=1}^n \begin{pmatrix}\mmz - \mmv_i \\ r\end{pmatrix} \in \cproduct_{i=1}^n \cc{Q}^{d+1},\\
                    & \mmv_i \in \Omega_i,\ \forall i \in [n],\\
                    & \mmz \in \conv(\{\Omega_i\}_{i=1}^n).
                \end{aligned}
                \]
            ''')
        ]
        geometry_sib_ftp[1].next_to(geometry_sib_ftp[0], DOWN, buff=0.25).to_edge(LEFT, buff=1.5)
        geometry_sib_ftp[2].next_to(geometry_sib_ftp[0], DOWN, buff=0.25).to_edge(LEFT, buff=1.5)

        self.play(FadeIn(geometry_sib_ftp[0], geometry_sib_ftp[1]))
        self.wait()
        self.next_slide()

        self.play(FadeIn(geometry_sib_ftp_question[1]), FadeOut(geometry_sib_ftp_question[0]))
        self.wait()
        self.next_slide()

        self.play(FadeIn(geometry_sib_ftp[2]), FadeOut(geometry_sib_ftp[1]))
        self.wait()
        self.next_slide()

        self.play(FadeIn(geometry_sib_ftp_question[2]), FadeOut(geometry_sib_ftp_question[1]))
        self.play(FadeOut(geometry_sib_problem[0], geometry_sib_problem[3]),
            Group(geometry_sib_ftp_question[2], geometry_sib_ftp[0], geometry_sib_ftp[2]).animate.next_to(subtitle_geometry, DOWN, buff=0.5).to_edge(LEFT, buff=1)
        )
        self.wait()
        self.next_slide()

        geometry_sib_ftp_thm = Theorem(r'''
            {\bf\underline{Thm:}} Let $D$ be the diameter of $\conv(\{\Omega_i\}_{i=1}^n)$.
            There is an iterative algorithm that solves FTP in $O({D^2 \log n \over \eps^2 \hat{r}^2})$ iterations.
        ''', edge_color=YELLOW).next_to(geometry_sib_ftp[2], DOWN, buff=1)
        geometry_sib_ftp_thm.shift([-geometry_sib_ftp_thm.get_center()[0], 0, 0])

        self.play(FadeIn(geometry_sib_ftp_thm))
        self.wait()
        self.next_slide()

        self.play(geometry_sib_ftp_thm.animate.scale(0.5).next_to(geometry_sib_claim, DOWN, buff=0.1).to_edge(RIGHT, buff=0.5))
        self.play(Group(geometry_sib_ftp_question[2], geometry_sib_ftp[0], geometry_sib_ftp[2]).animate.scale(0.7).next_to(geometry_sib_ftp_thm, DOWN, buff=0.25).to_edge(RIGHT, buff=1))
        self.wait()
        self.next_slide()

        geometry_ftp_proof_reduction = [
            MyTex(r'''\scalebox{0.8}{\parbox{15cm}{
            1. Reduction to zero-sum game
            }}''', up=subtitle_geometry).set_color(YELLOW),
        ]
        geometry_ftp_proof_reduction.append( # 1
            MyTex(r'''\scalebox{0.8}{\parbox{15cm}{
            $\displaystyle \cc{K} = \cproduct_{i=1}^n \cc{Q}^{d+1},\ \brmf(\mmz, \mmv_1, \dots, \mmv_n, r) = \cproduct_{i=1}^n \begin{pmatrix}\mmz - \mmv_i \\ r\end{pmatrix}$
            }}''', up=geometry_ftp_proof_reduction[-1], buff=0.25)
        )
        geometry_ftp_proof_reduction.append( # 2
            MyTex(r'''\scalebox{0.8}{\parbox{15cm}{
            $\displaystyle \brmf(\mmz, \mmv_1, \dots, \mmv_n, r) \bullet \mmy \ge 0,\ \forall \mmy \in \cc{B} \subseteq \cc{K}$
            }}''', up=geometry_ftp_proof_reduction[-1], buff=0.25)
        )
        geometry_ftp_proof_reduction.append( # 3
            MyTex(r'''\scalebox{0.8}{\parbox{15cm}{
            $\displaystyle \cc{A} = \Big\{(\mmz, \mmv_1, \dots, \mmv_n, r) : \mmz \in \conv(\{\Omega_i\}_{i=1}^n),\ \mmv_i \in \Omega_i, \forall i \in [n], \ r \le \hat{r} \Big\}$
            }}''', up=geometry_ftp_proof_reduction[-1], buff=0.25)
        )
        geometry_ftp_proof_reduction.append( # 4
            MyTex(r'''\scalebox{0.8}{\parbox{15cm}{
            Let $\cc{O}^*$ be the optimal set. If $\hat{r}\ge r^*$, $\cc{O}^* \cap \cc{A} \ne \varnothing$.
            }}''', up=geometry_ftp_proof_reduction[-1], buff=0.25)
        )
        geometry_ftp_proof_reduction.append( # 5
            MyTex(r'''\scalebox{0.8}{\parbox{15cm}{
            Let $\mmx = (\mmz, \mmv_1, \dots, \mmv_n, r)$:
            \begin{myitemize}
            \item If $\hat{r} \ge r^*$, then $\displaystyle \max_{\mmx\in\cc{A}} \min_{\mmy\in\cc{B}}\ \brmf(\mmx) \bullet \mmy = \lambda^* \ge 0$. 
            \item If $\lambda^* < 0$, then $\cc{O}^* \cap \cc{A} = \varnothing$ and $\hat{r} < r^*$.
            \end{myitemize}
            }}''', up=geometry_ftp_proof_reduction[-1], buff=0.25)
        )

        self.play(FadeIn(geometry_ftp_proof_reduction[0]))
        self.wait()
        self.next_slide()

        self.play(FadeIn(geometry_ftp_proof_reduction[1]))
        self.wait()
        self.next_slide()

        self.play(FadeIn(geometry_ftp_proof_reduction[2]))
        self.wait()
        self.next_slide()

        self.play(FadeIn(geometry_ftp_proof_reduction[3]))
        self.wait()
        self.next_slide()

        self.play(FadeIn(geometry_ftp_proof_reduction[4]))
        self.wait()
        self.next_slide()

        self.play(FadeIn(geometry_ftp_proof_reduction[5]))
        self.wait()
        self.next_slide()

        self.play(
            FadeOut(*geometry_ftp_proof_reduction[1:5]),
            geometry_ftp_proof_reduction[5].animate.next_to(geometry_ftp_proof_reduction[0], DOWN, buff=0.25).to_edge(LEFT, buff=1))
        self.wait()
        self.next_slide()

        geometry_ftp_proof_reduction.append( # 6
            MyTex(r'''\scalebox{0.8}{\parbox{15cm}{
            Solve the game up to an additive error of $\eps\hat{r} \over \sqrt{2}$:
            \begin{myitemize}
            \item If there exist $t$: $\displaystyle \max_{\mmx \in \cc{A}}\ \brmf(\mmx) \bullet \xt{\mmy}{t} < 0 \quad \Rightarrow \quad \lambda^* < 0 \text{ and } \hat{r} < r^*$
            \end{myitemize}
            }}''', up=geometry_ftp_proof_reduction[-1], buff=0.4)
        )

        geometry_ftp_proof_reduction.append( # 7
            MyTex(r'''\scalebox{0.8}{\parbox{15cm}{
            \begin{myitemize}
            \item Conversely, if $\brmf(\xt{\mmx}{t}) \bullet \xt{\mmy}{t}\ge 0$ for all $t = 1, \dots, T$:
                \begin{myitemize}
                \item $\displaystyle 0 \le {1\over T} \sum_{t=1}^T \brmf(\xt{\mmx}{t}) \bullet \xt{\mmy}{t}$
                \end{myitemize}
            \end{myitemize}
            }}''', up=geometry_ftp_proof_reduction[-1], buff=0.25)
        )

        geometry_ftp_proof_reduction.append( # 8
            MyTex(r'''\scalebox{0.8}{\parbox{15cm}{
            \begin{myitemize}
            \item Conversely, if $\brmf(\xt{\mmx}{t}) \bullet \xt{\mmy}{t}\ge 0$ for all $t = 1, \dots, T$:
                \begin{myitemize}
                \item $\displaystyle 0 \le {1\over T} \sum_{t=1}^T \brmf(\xt{\mmx}{t}) \bullet \xt{\mmy}{t} \le \lambda_{\min}\big(\brmf(\tilde{\mmx})\big) + {\eps\hat{r}\over \sqrt{2}}$
                \end{myitemize}
            \end{myitemize}
            }}''', up=geometry_ftp_proof_reduction[-2], buff=0.25)
        )

        geometry_ftp_proof_reduction.append( # 9
            MyTex(r'''\scalebox{0.8}{\parbox{15cm}{
            \begin{myitemize}
            \item Conversely, if $\brmf(\xt{\mmx}{t}) \bullet \xt{\mmy}{t}\ge 0$ for all $t = 1, \dots, T$:
                \begin{myitemize}
                \item $\displaystyle 0 \le \lambda_{\min}\big( \cproduct_{i=1}^n (\tilde{\mmz} - \tilde{\mmv}_i, \tilde{r}) \big) + {\eps\hat{r}\over \sqrt{2}}$
                \end{myitemize}
            \end{myitemize}
            }}''', up=geometry_ftp_proof_reduction[-3], buff=0.25)
        )

        geometry_ftp_proof_reduction.append( # 10
            MyTex(r'''\scalebox{0.8}{\parbox{15cm}{
            \begin{myitemize}
            \item Conversely, if $\brmf(\xt{\mmx}{t}) \bullet \xt{\mmy}{t}\ge 0$ for all $t = 1, \dots, T$:
                \begin{myitemize}
                \item $\displaystyle \cproduct_{i=1}^n \begin{pmatrix} \tilde{\mmz} - \tilde{\mmv}_i\\ \tilde{r} \end{pmatrix} + {\eps\hat{r}\over \sqrt{2}} \cproduct_{i=1}^n \begin{pmatrix}\mmzero\\ \sqrt{2} \end{pmatrix} \in \cproduct_{i=1}^n \cc{Q}^{d+1}$
                \end{myitemize}
            \end{myitemize}
            }}''', up=geometry_ftp_proof_reduction[-4], buff=0.25)
        )

        geometry_ftp_proof_reduction.append( # 11
            MyTex(r'''\scalebox{0.8}{\parbox{15cm}{
            \begin{myitemize}
            \item Conversely, if $\brmf(\xt{\mmx}{t}) \bullet \xt{\mmy}{t}\ge 0$ for all $t = 1, \dots, T$:
                \begin{myitemize}
                \item $\displaystyle \cproduct_{i=1}^n \begin{pmatrix} \tilde{\mmz} - \tilde{\mmv}_i\\ \tilde{r} + \eps\hat{r} \end{pmatrix} \in \cproduct_{i=1}^n \cc{Q}^{d+1}$
                \end{myitemize}
            \end{myitemize}
            }}''', up=geometry_ftp_proof_reduction[-5], buff=0.25)
        )

        geometry_ftp_proof_reduction.append( # 12
            MyTex(r'''\scalebox{0.8}{\parbox{15cm}{
            \begin{myitemize}
            \item Conversely, if $\brmf(\xt{\mmx}{t}) \bullet \xt{\mmy}{t}\ge 0$ for all $t = 1, \dots, T$:
                \begin{myitemize}
                \item $\displaystyle \cproduct_{i=1}^n \begin{pmatrix} \tilde{\mmz} - \tilde{\mmv}_i\\ \tilde{r} + \eps\hat{r} \end{pmatrix} \in \cproduct_{i=1}^n \cc{Q}^{d+1}$
                \item $(\tilde{\mmz}, \tilde{\mmv}_1, \dots, \tilde{\mmv}_n, \tilde{r} + \eps\hat{r})$ is a solution to FTP
                \end{myitemize}
            \end{myitemize}
            }}''', up=geometry_ftp_proof_reduction[-6], buff=0.25)
        )

        self.play(FadeIn(geometry_ftp_proof_reduction[6]))
        self.wait()
        self.next_slide()

        self.play(FadeIn(geometry_ftp_proof_reduction[7]))
        self.wait()
        self.next_slide()

        for i in range(7, 12):
            self.play(FadeOut(geometry_ftp_proof_reduction[i]), FadeIn(geometry_ftp_proof_reduction[i+1]))
            self.wait()
            self.next_slide()

        self.play(FadeOut(
            geometry_ftp_proof_reduction[0],
            geometry_ftp_proof_reduction[5],
            geometry_ftp_proof_reduction[6],
            geometry_ftp_proof_reduction[12]
        ))

        geometry_ftp_proof_oracle = [
            MyTex(r'''\scalebox{0.8}{\parbox{15cm}{
            2. Implementation of {\sc Oracle}
            }}''', up=subtitle_geometry).set_color(YELLOW),
        ]

        geometry_ftp_proof_oracle.append( # 1
            MyTex(r'''\scalebox{0.8}{\parbox{15cm}{
            $\displaystyle \brmf(\mmx) = \cproduct_{i=1}^n \begin{pmatrix} \mmz - \mmv_i\\ r \end{pmatrix},\ \mmy = \cproduct_{i=1}^n \begin{pmatrix} \bar{\mmy}_i \\ y_{i,0} \end{pmatrix}$
            }}''', up=geometry_ftp_proof_oracle[-1], buff=0.25)
        )

        geometry_ftp_proof_oracle.append( # 2
            MyTex(r'''\scalebox{0.8}{\parbox{15cm}{
            $\displaystyle \brmf(\mmx) \bullet \mmy = \big(\sum_{i=1}^n \bar{\mmy}_i \big)^T \mmz - \sum_{i=1}^n \bar{\mmy}_i^T \mmv_i + \big(\sum_{i=1}^n y_{i,0}\big)r$
            }}''', up=geometry_ftp_proof_oracle[-1], buff=0.25)
        )

        geometry_ftp_proof_oracle.append( # 3
            MyTex(r'''\scalebox{0.8}{\parbox{15cm}{
            The {\sc Oracle} problem:
            \begin{myitemize}
            \item $\max\ \brmf(\mmx) \bullet \mmy \hspace{1em} {\rm s.t.}\ \mmx \in \cc{A}$
            \end{myitemize}
            }}''', up=geometry_ftp_proof_oracle[-1], buff=0.25)
        )

        geometry_ftp_proof_oracle.append( # 4
            MyTex(r'''\scalebox{0.8}{\parbox{15cm}{
            The {\sc Oracle} problem:
            \begin{myitemize}
            \item[] $\displaystyle
            \begin{aligned}
                \underset{\mmz, \mmv_1, \dots, \mmv_n, r}{\rm maximize}\quad & \big(\sum_{i=1}^n \bar{\mmy}_i \big)^T \mmz - \sum_{i=1}^n \bar{\mmy}_i^T \mmv_i + \big(\sum_{i=1}^n y_{i,0}\big)r\\
                {\rm subject\ to} \quad
                & \mmz \in \conv(\{\Omega_i\}_{i=1}^n),\\
                & \mmv_i \in \Omega_i, \ \forall i \in [n],\\
                & r \le \hat{r}.
            \end{aligned}
            $
            \end{myitemize}
            }}''', up=geometry_ftp_proof_oracle[-2], buff=0.25)
        )

        self.play(FadeIn(geometry_ftp_proof_oracle[0]))
        self.wait()
        self.next_slide()

        self.play(FadeIn(geometry_ftp_proof_oracle[1]))
        self.wait()
        self.next_slide()

        self.play(FadeIn(geometry_ftp_proof_oracle[2]))
        self.wait()
        self.next_slide()

        self.play(FadeIn(geometry_ftp_proof_oracle[3]))
        self.wait()
        self.next_slide()

        self.play(FadeIn(geometry_ftp_proof_oracle[4]), FadeOut(geometry_ftp_proof_oracle[3]))
        self.wait()
        self.next_slide()

        self.play(FadeOut(*geometry_ftp_proof_oracle[1:3]),
            geometry_ftp_proof_oracle[4].animate.next_to(geometry_ftp_proof_oracle[0], DOWN, buff=0.25).to_edge(LEFT, buff=1)
        )
        self.wait()
        self.next_slide()
        
        geometry_ftp_proof_oracle.append( # 5
            MyTex(r'''\scalebox{0.8}{\parbox{15cm}{
            The problems for $\mmz$, each $\mmv_i$ and $r$ can be solved separately!
            }}''', up=geometry_ftp_proof_oracle[-1], buff=0.25).set_color(GREEN)
        )

        self.play(FadeIn(geometry_ftp_proof_oracle[5]))
        self.wait()
        self.next_slide()
        
        geometry_ftp_proof_oracle.append( # 6
            MyTex(r'''\scalebox{0.8}{\parbox{15cm}{
            \begin{myitemize}
            \item For $\mmz$, let $\displaystyle \mmh = \sum_{i=1}^n \bar{\mmy}_i$, the subproblem is
                $\displaystyle \max\Big\{ \mmh^T \mmz : \mmz \in \conv(\{\Omega_i\}_{i=1}^n) \Big\}$
            \end{myitemize}
            }}''', up=geometry_ftp_proof_oracle[-1], buff=0.25)
        )

        geometry_ftp_proof_oracle.append( # 7
            MyTex(r'''\scalebox{0.8}{\parbox{15cm}{
            \begin{myitemize}
            \item For $\mmz$, let $\displaystyle \mmh = \sum_{i=1}^n \bar{\mmy}_i$, the subproblem is
                $\displaystyle \max_{i\in [n]}\Big( \max \big\{ \mmh^T \mmz : \mmz \in \Omega_i \big\} \Big)$
            \end{myitemize}
            }}''', up=geometry_ftp_proof_oracle[-2], buff=0.25)
        )

        self.play(FadeIn(geometry_ftp_proof_oracle[6]))
        self.wait()
        self.next_slide()

        self.play(FadeIn(geometry_ftp_proof_oracle[7]), FadeOut(geometry_ftp_proof_oracle[6]))
        self.wait()
        self.next_slide()

        geometry_ftp_proof_oracle.append( # 8
            MyTex(r'''\scalebox{0.8}{\parbox{15cm}{
            \begin{myitemize}
            \item For $\mmz$, let $\displaystyle \mmh = \sum_{i=1}^n \bar{\mmy}_i$, the subproblem is
                $\displaystyle \max_{i\in [n]}\Big( \max \big\{ \mmh^T \mmz : \mmz \in \Omega_i \big\} \Big)$
            \item For $\mmv_i$, the subproblem is $\min\big\{\bar{\mmy}_i^T \mmv_i : \mmv_i \in \Omega_i \big\}$
            \end{myitemize}
            }}''', up=geometry_ftp_proof_oracle[-3], buff=0.25)
        )

        self.play(FadeIn(geometry_ftp_proof_oracle[8]), FadeOut(geometry_ftp_proof_oracle[7]))
        self.wait()
        self.next_slide()

        geometry_ftp_proof_oracle.append( # 9
            MyTex(r'''\scalebox{0.8}{\parbox{15cm}{
            \begin{myitemize}
            \item For $\mmz$, let $\displaystyle \mmh = \sum_{i=1}^n \bar{\mmy}_i$, the subproblem is
                $\displaystyle \max_{i\in [n]}\Big( \max \big\{ \mmh^T \mmz : \mmz \in \Omega_i \big\} \Big)$
            \item For $\mmv_i$, the subproblem is $\min\big\{\bar{\mmy}_i^T \mmv_i : \mmv_i \in \Omega_i \big\}$
            \item For $r$, $r = \hat{r}$
            \end{myitemize}
            }}''', up=geometry_ftp_proof_oracle[-4], buff=0.25)
        )

        self.play(FadeIn(geometry_ftp_proof_oracle[9]), FadeOut(geometry_ftp_proof_oracle[8]))
        self.wait()
        self.next_slide()

        geometry_ftp_proof_width = [
            MyTex(r'''\scalebox{0.8}{\parbox{15cm}{
            3. Width of {\sc Oracle}
            }}''', up=subtitle_geometry).set_color(YELLOW),
        ]

        geometry_ftp_proof_width.append( # 1
            MyTex(r'''\scalebox{0.8}{\parbox{15cm}{
            Let $(\mmz, \mmv_1, \dots, \mmv_n, r)$ be the output of {\sc Oracle}:
            \begin{myitemize}
            \item[] $\displaystyle 
                \begin{aligned}
                    \Big\|\cproduct_{i=1}^n (\mmz - \mmv_i, r)\Big\|_\infty 
                    &= \max_{k\in [2n]}\ \Big|\lambda_{k}\big(\cproduct_{i=1}^n (\mmz - \mmv_i, r)\big) \Big| \\
                    &\le {1\over \sqrt{2}} \max_{i\in [n]}\ \|\mmz - \mmv_i\| + r\\
                    &\le {1\over \sqrt{2}} (D + \hat{r})\\
                    &\le \sqrt{2} D.
                \end{aligned}$
            \end{myitemize}
            }}''', up=geometry_ftp_proof_width[-1], buff=0.25)
        )

        self.play(FadeOut(
            geometry_ftp_proof_oracle[9],
            geometry_ftp_proof_oracle[5],
            geometry_ftp_proof_oracle[4],
            geometry_ftp_proof_oracle[0]
            ),
            FadeIn(geometry_ftp_proof_width[0])
        )
        self.wait()
        self.next_slide()

        self.play(FadeIn(geometry_ftp_proof_width[1]))
        self.wait()
        self.next_slide()

        geometry_ftp_proof_time = [
            MyTex(r'''\scalebox{0.8}{\parbox{15cm}{
            4. Running time analysis
            }}''', up=subtitle_geometry).set_color(YELLOW),
        ]

        self.play(FadeOut(
                *geometry_ftp_proof_width
            ),
            FadeIn(geometry_ftp_proof_time[0])
        )
        self.wait()
        self.next_slide()

        geometry_ftp_proof_time.append( # 1
            MyTex(r'''\scalebox{0.8}{\parbox{15cm}{
            Number of iterations:
            }}''', up=geometry_ftp_proof_time[-1], buff=0.25).set_color(GREEN)
        )

        self.play(FadeIn(geometry_ftp_proof_time[-1]))
        self.wait()
        self.next_slide()

        geometry_ftp_proof_time.append( # 2
            MyTex(r'''\scalebox{0.8}{\parbox{15cm}{
            \begin{myitemize}
            \item $\rho = \sqrt{2}D,\ r = 2n,\ \eps = {\eps\hat{r}\over \sqrt{2}} \quad \Rightarrow \quad T = \lceil{16 D^2 \ln(2n) \over \eps^2 \hat{r}^2}\rceil$
            \end{myitemize}
            }}''', up=geometry_ftp_proof_time[-1], buff=0.25)
        )
        geometry_ftp_proof_time[-1][0][-21:].set_color(RED)

        self.play(FadeIn(geometry_ftp_proof_time[-1]))
        self.wait()
        self.next_slide()

        geometry_ftp_proof_time.append( # 3
            MyTex(r'''\scalebox{0.8}{\parbox{15cm}{
            Symmetric cone multiplicative weights update:
            }}''', up=geometry_ftp_proof_time[-1], buff=0.25).set_color(GREEN)
        )

        self.play(FadeIn(geometry_ftp_proof_time[-1]))
        self.wait()
        self.next_slide()

        geometry_ftp_proof_time.append( # 4
            MyTex(r'''\scalebox{0.8}{\parbox{15cm}{
            \begin{myitemize}
            \item $\displaystyle \xt{\mmy}{t+1} = \frac
                {\mmexp(-\frac{\eta}{\rho}\sum_{\tau = 1}^{t} \brmf(\xt{\mmx}{\tau}))}
                {\Tr\big(\mmexp(-\frac{\eta}{\rho}\sum_{\tau = 1}^{t} \brmf(\xt{\mmx}{\tau}))\big)}
                \in \cproduct_{i=1}^n \cc{Q}^{d+1} \quad \Rightarrow \quad O(nd)$
            \end{myitemize}
            }}''', up=geometry_ftp_proof_time[-1], buff=0.25)
        )
        geometry_ftp_proof_time[-1][0][-6:].set_color(RED)

        self.play(FadeIn(geometry_ftp_proof_time[-1]))
        self.wait()
        self.next_slide()

        geometry_ftp_proof_time.append( # 5
            MyTex(r'''\scalebox{0.8}{\parbox{15cm}{
            The {\sc Oracle} process:
            }}''', up=geometry_ftp_proof_time[-1], buff=0.25).set_color(GREEN)
        )

        self.play(FadeIn(geometry_ftp_proof_time[-1]))
        self.wait()
        self.next_slide()

        geometry_ftp_proof_time.append( # 6
            MyTex(r'''\scalebox{0.8}{\parbox{15cm}{
            \begin{myitemize}
            \item Computing $\displaystyle \mmh = \sum_{i=1}^n \bar{\mmy}_i \quad \Rightarrow \quad O(nd)$
            \end{myitemize}
            }}''', up=geometry_ftp_proof_time[-1], buff=0.25)
        )
        geometry_ftp_proof_time[-1][0][-6:].set_color(RED)

        self.play(FadeIn(geometry_ftp_proof_time[-1]))
        self.wait()
        self.next_slide()

        geometry_ftp_proof_time.append( # 7
            MyTex(r'''\scalebox{0.8}{\parbox{15cm}{
            \begin{myitemize}
            \item Solving $\displaystyle \max_{i\in [n]}\Big( \max\big\{\mmh^T \mmz : \mmz \in \Omega_i\big\} \Big) \quad \Rightarrow \quad O(S)$
            \end{myitemize}
            }}''', up=geometry_ftp_proof_time[-1], buff=0.25)
        )
        geometry_ftp_proof_time[-1][0][-5:].set_color(RED)

        self.play(FadeIn(geometry_ftp_proof_time[-1]))
        self.wait()
        self.next_slide()

        geometry_ftp_proof_time.append( # 8
            MyTex(r'''\scalebox{0.8}{\parbox{15cm}{
            \begin{myitemize}
            \item Solving $\displaystyle \min\big\{\bar{\mmy}_i^T \mmv_i : \mmv_i \in \Omega_i\big\}$ for $i=1,\dots, n \quad \Rightarrow \quad O(S)$
            \end{myitemize}
            }}''', up=geometry_ftp_proof_time[-1], buff=0.25)
        )
        geometry_ftp_proof_time[-1][0][-5:].set_color(RED)

        self.play(FadeIn(geometry_ftp_proof_time[-1]))
        self.wait()
        self.next_slide()

        geometry_sib_opt_thm = Theorem(r'''
        {\bf\underline{Thm:}}
        Let $R$ be the ratio ${D \over r^*}$. There is an algorithm that computes an $(1 + \eps)$-approximate SIB in $O({R^2 (S + nd) \log n \over \eps^2})$ time.
        ''', edge_color=RED)

        self.play(
            FadeOut(*geometry_ftp_proof_time, Group(geometry_sib_ftp_question[2], geometry_sib_ftp[0], geometry_sib_ftp[2])),
            FadeIn(geometry_sib_opt_thm)
        )
        self.wait()
        self.next_slide()

        self.play(
            geometry_sib_opt_thm.animate.scale(0.5).next_to(geometry_sib_ftp_thm, DOWN, buff=0.1).to_edge(RIGHT, buff=0.5)
        )
        self.wait()
        self.next_slide()

        geometry_sib_opt_proof = [
            MyTex(r'''\scalebox{0.8}{\parbox{15cm}{
            1. From FTP to optimization
            }}''', up=subtitle_geometry).set_color(RED),
        ]

        self.play(FadeIn(geometry_sib_opt_proof[-1]))
        self.wait()
        self.next_slide()

        geometry_sib_opt_proof.append( # 1
            MyTex(r'''\scalebox{0.8}{\parbox{15cm}{
            Adaptively choose $\hat{r}$ and $\eps$
            }}''', up=geometry_sib_opt_proof[-1], buff=0.25)
        )

        self.play(FadeIn(geometry_sib_opt_proof[-1]))
        self.wait()
        self.next_slide()

        geometry_sib_opt_proof.append( # 2
            MyTex(r'''\scalebox{0.8}{\parbox{15cm}{
            2. How to compute the diameter $D$?
            }}''', up=geometry_sib_opt_proof[-1], buff=0.5).set_color(RED)
        )

        self.play(FadeIn(geometry_sib_opt_proof[-1]))
        self.wait()
        self.next_slide()
        
        geometry_sib_opt_proof.append( # 3
            MyTex(r'''\scalebox{0.8}{\parbox{15cm}{
            2. How to compute the diameter $D$? We don't!
            }}''', up=geometry_sib_opt_proof[-2], buff=0.5).set_color(RED)
        )

        self.play(FadeIn(geometry_sib_opt_proof[-1]), FadeOut(geometry_sib_opt_proof[-2]))
        self.wait()
        self.next_slide()

        geometry_sib_opt_proof.append( # 4
            MyTex(r'''\scalebox{0.8}{\parbox{15cm}{
            An upper bound on $r^*$:
            \begin{myitemize}
            \item Pick $\mmv_i \in \Omega_i$, compute $\displaystyle E = \max_{i\in [n]} \|\mmv_1 - \mmv_i\|$, then $r^* \le E \le D$
            \end{myitemize}
            }}''', up=geometry_sib_opt_proof[-1], buff=0.25)
        )

        self.play(FadeIn(geometry_sib_opt_proof[-1]))
        self.wait()
        self.next_slide()

        geometry_sib_opt_proof.append( # 5
            MyTex(r'''\scalebox{0.8}{\parbox{15cm}{
            An upper bound on $\|\brmf(\xt{\mmx}{t})\|_\infty$:
            \begin{myitemize}
            \item Use the doubling trick
            \item $\rho_1 = \sqrt{2}E$, $\rho_\tau = 2 \rho_{\tau - 1}$
            \end{myitemize}
            }}''', up=geometry_sib_opt_proof[-1], buff=0.25)
        )

        self.play(FadeIn(geometry_sib_opt_proof[-1]))
        self.wait()
        self.next_slide()

        self.play(FadeOut(
                *geometry_sib_opt_proof[:2], 
                *geometry_sib_opt_proof[3:],
                geometry_sib_claim,
                geometry_sib_ftp_thm
            ),
            geometry_sib_opt_thm.animate.to_edge(UR, buff=0.5)
        )
        self.wait()
        self.next_slide()

        geometry_sib_examples = [
            MyTex(r'''\scalebox{0.9}{\parbox{15cm}{
            Some examples
            }}''', up=subtitle_geometry).set_color(RED),
        ]

        self.play(FadeIn(geometry_sib_examples[-1]))
        self.wait()
        self.next_slide()

        geometry_sib_examples.append( # 1
            MyTex(r'''\scalebox{0.8}{\parbox{15cm}{
            Convex polytopes: $O(S) = O(N)$
            \begin{myitemize}
            \item Polytopes distance: $O({R^2 (N + d) \over \eps^2})$
            \item Smallest enclosing ball: $O({nd \log n \over \eps^2})$
            \item SIB of line segments: $O({R^2 nd \log n \over \eps^2})$
            \end{myitemize}
            }}''', up=geometry_sib_examples[-1], buff=0.25)
        )
        geometry_sib_examples[-1][0][:16].set_color(BLUE)

        self.play(FadeIn(geometry_sib_examples[-1]))
        self.wait()
        self.next_slide()

        geometry_sib_examples.append( # 2
            MyTex(r'''\scalebox{0.8}{\parbox{15cm}{
            Reduced polytopes: $O(S) = O(N)$
            \begin{myitemize}
            \item $C$-SVM, $\nu$-SVM: $O({R^2 (N + d) \over \eps^2})$
            \end{myitemize}
            }}''', up=geometry_sib_examples[-1], buff=0.25)
        )
        geometry_sib_examples[-1][0][:17].set_color(BLUE)

        self.play(FadeIn(geometry_sib_examples[-1]))
        self.wait()
        self.next_slide()

        geometry_sib_examples.append( # 3
            MyTex(r'''\scalebox{0.8}{\parbox{15cm}{
            Axis-aligned bounding boxes (AABBs): $O(S) = O(nd)$
            }}''', up=geometry_sib_examples[-1], buff=0.25)
        )
        geometry_sib_examples[-1][0][:33].set_color(BLUE)

        self.play(FadeIn(geometry_sib_examples[-1]))
        self.wait()
        self.next_slide()

        geometry_sib_examples.append( # 4
            MyTex(r'''\scalebox{0.8}{\parbox{15cm}{
            Balls: $O(S) = O(nd)$
            }}''', up=geometry_sib_examples[-1], buff=0.25)
        )
        geometry_sib_examples[-1][0][:6].set_color(BLUE)

        self.play(FadeIn(geometry_sib_examples[-1]))
        self.wait()
        self.next_slide()

        geometry_sib_examples.append( # 5
            MyTex(r'''\scalebox{0.8}{\parbox{15cm}{
            Ellipsoids: $O(S) = O(nd^2)$, assuming matrix inverses are pre-computed
            }}''', up=geometry_sib_examples[-1], buff=0.25)
        )
        geometry_sib_examples[-1][0][:11].set_color(BLUE)

        self.play(FadeIn(geometry_sib_examples[-1]))
        self.wait()
        self.next_slide()

        geometry_sib_takeaway = MyTex(r'''
            Takeaway: If we can solve linear optimization problems over every $\Omega_i$, then we can also solve the SIB problem approximately. 
        ''', up=subtitle_geometry, buff=2)
        geometry_sib_takeaway[0][:9].set_color(RED)

        self.play(FadeOut(*geometry_sib_examples), FadeIn(geometry_sib_takeaway))
        self.wait()
        self.next_slide()

        geometry_sib_extension = MyTex(r'''
            Another example: The input objects can be convex hulls of compact (but not necessarily convex) objects.
        ''', up=geometry_sib_takeaway, buff=0.5)
        geometry_sib_extension[0][:15].set_color(RED)

        self.play(FadeIn(geometry_sib_extension))
        self.wait()
        self.next_slide()

        self.play(FadeOut(geometry_sib_extension, geometry_sib_takeaway, geometry_sib_opt_thm, geoemtry_subtitle_sib))

        geometry_others = [
            MyTex(r'''\scalebox{0.9}{\parbox{15cm}{
                Polytope distance (Hard-SVM)
                \begin{myitemize}
                \item[] $
                \displaystyle
                \begin{aligned}[t]
                \minimize_{\mmgamma,\ \mmmu}\quad & \|\mmP\mmgamma - \mmQ\mmmu\|\\
                \subto\quad & \mmone^T \mmgamma = 1, \ \mmgamma \ge 0, \\
                & \mmone^T \mmmu = 1, \ \mmmu \ge 0
                \end{aligned}
                \hspace{3em}
                \begin{aligned}[t]
                \maximize_{\mmw, s_1, s_2}\quad & s_1 + s_2 \\
                \subto\quad & \mmP^T \mmw - s_1 \mmone \ge 0,  \\
                & -\mmQ^T \mmw - s_2 \mmone \ge 0, \\
                & \|\mmw\| \le 1
                \end{aligned}
                $
                \end{myitemize}
            }}''', up=subtitle_geometry)
        ]

        geometry_others[-1][0][:26].set_color(BLUE)
        
        geometry_others.append(
            MyTex(r'''\scalebox{0.9}{\parbox{15cm}{
                SEB of balls (SEBB)
                \begin{myitemize}
                \item[] $
                \displaystyle
                \begin{aligned}[t]
                \minimize_{\mmz,\ r} \quad & r\\
                \subto\quad & \|\mmz - \mmp_i\| \le r - r_i,\ \forall i \in [n]
                \end{aligned}
                $
                \end{myitemize}
            }}''', up=geometry_others[-1])
        )

        geometry_others[-1][0][:16].set_color(BLUE)
        
        geometry_others.append(
            MyTex(r'''\scalebox{0.9}{\parbox{15cm}{
                Soft-margin SIB
                \begin{myitemize}
                \item[] $
                \displaystyle
                \begin{aligned}[t]
                \underset{\mmz, \mmv_1, \dots, \mmv_n, \mmxi, r}{\rm minimize} \quad
                & r + C \sum_{i=1}^n \xi_i\\
                {\rm subject\ to} \quad
                & \|\mmz - \mmv_i\| \le r + \xi_i,\ \forall i \in [n],\\
                & \mmv_i \in \Omega_i,\ \forall i \in [n],\\
                & \mmxi\ge 0,\ r \ge 0
                \end{aligned}
                $
                \end{myitemize}
            }}''')
        )

        geometry_others[-1][0][:14].set_color(BLUE)
        geometry_others[-1].next_to(geometry_others[-2], RIGHT, buff=1)
        geometry_others[-1].shift([0, geometry_others[-2].get_top()[1] - geometry_others[-1].get_top()[1], 0])

        self.play(FadeIn(geometry_others[0]))
        self.wait()
        self.next_slide()

        self.play(FadeIn(geometry_others[1]))
        self.wait()
        self.next_slide()

        self.play(FadeIn(geometry_others[2]))
        self.wait()
        self.next_slide()
        
        self.play(FadeOut(*geometry_others))


#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        # # 1. Polytope Distance / Hard-SVM
        # self.play(Create(geoemtry_subtitles[0]))
        # self.wait()
        # self.next_slide()

        # geometry_pd_p_hall = Polygon(*np.c_[pd.p_points_hall, np.zeros(pd.p_points_hall.shape[0])], color=YELLOW)
        # geometry_pd_q_hall = Polygon(*np.c_[pd.q_points_hall, np.zeros(pd.q_points_hall.shape[0])], color=BLUE)

        # geometry_pd_p_dots = [Dot([*pd.p_points[i], 0], color=YELLOW) for i in range(len(pd.p_points))]
        # geometry_pd_q_dots = [Dot([*pd.q_points[i], 0], color=BLUE) for i in range(len(pd.q_points))]

        # geometry_pd_p_dots_group = Group(*geometry_pd_p_dots)
        # geometry_pd_q_dots_group = Group(*geometry_pd_q_dots)

        # geometry_pd_p_tex = MyTex(r'$\cc{P}$').scale(1.5).next_to(geometry_pd_p_dots_group, DOWN, buff=0.5).set_color(YELLOW)
        # geometry_pd_q_tex = MyTex(r'$\cc{Q}$').scale(1.5).next_to(geometry_pd_q_dots_group, DOWN, buff=0.5).set_color(BLUE)

        # geometry_pd_opt_line = Line(*pd.optimal_line_seg, color=RED)

        # geometry_pd_draw_group = Group(geometry_pd_p_dots_group, geometry_pd_q_dots_group, geometry_pd_p_hall, geometry_pd_q_hall, geometry_pd_opt_line, geometry_pd_p_tex, geometry_pd_q_tex)

        # geometry_svm_line = Line(*pd.optimal_svm_line, color=RED)
        # geometry_svm_draw_subgroup = Group(geometry_pd_p_dots_group.copy(), geometry_pd_q_dots_group.copy(), geometry_pd_p_hall.copy(), geometry_pd_q_hall.copy(), geometry_pd_p_tex.copy(), geometry_pd_q_tex.copy())
        # geometry_svm_draw_group = Group(geometry_svm_draw_subgroup, geometry_svm_line)

        # self.play(FadeIn(geometry_pd_p_dots_group, geometry_pd_q_dots_group, geometry_pd_p_tex, geometry_pd_q_tex))
        
        # self.wait()
        # self.next_slide()

        # self.play(Create(geometry_pd_p_hall), Create(geometry_pd_q_hall))
        # self.wait()
        # self.next_slide()

        # self.play(Create(geometry_pd_opt_line))
        # self.wait()
        # self.next_slide()

        # geometry_pd_prob = [
        #     MyTex(r'''
        #     Polytope distance:
        #     ''', up=subtitle_geometry).set_color(YELLOW),
        #     MyTex(r'''
        #     \[
        #     \begin{aligned}
        #         \minimize_{\mmgamma,\ \mmmu}\quad & \|\mmP\mmgamma - \mmQ\mmmu\|\\
        #         \subto\quad & \mmone^T \mmgamma = 1, \ \mmgamma \ge 0, \\
        #         & \mmone^T \mmmu = 1, \ \mmmu \ge 0.
        #     \end{aligned}
        #     \]
        #     ''')
        # ]
        # geometry_pd_prob[1].next_to(geometry_pd_prob[0], DOWN, buff=0.25).to_edge(LEFT, 1.5)
        # geometry_pd_prob = Group(*geometry_pd_prob)

        # self.play(FadeIn(geometry_pd_prob), geometry_pd_draw_group.animate.scale(0.4).next_to(geometry_pd_prob, RIGHT).to_edge(RIGHT, buff=3))
        # self.wait()
        # self.next_slide()


        # geometry_svm_prob_tex = [
        #     MyTex(r'''
        #     Support vector machine:
        #     ''', up=geometry_pd_prob).set_color(YELLOW),
        #     MyTex(r'''
        #     \[
        #     \begin{aligned}
        #     \maximize_{\mmw, s_1, s_2}\quad & s_1 + s_2                             \\
        #     \subto\quad                & \mmP^T \mmw - s_1 \mmone \ge 0,  \\
        #                                 & -\mmQ^T \mmw - s_2 \mmone \ge 0, \\
        #                                 & \|\mmw\| \le 1.
        #     \end{aligned}
        #     \]
        #     '''),
        #     MyTex(r'''
        #     \[
        #     \begin{aligned}
        #     \maximize_{\mmw, s_1, s_2}\quad & s_1 + s_2                             \\
        #     \subto\quad                & \mmP^T \mmw - s_1 \mmone \in \bR^{m_1}_+,  \\
        #                                 & -\mmQ^T \mmw - s_2 \mmone \in \bR^{m_2}_+, \\
        #                                 & \|\mmw\| \le 1.
        #     \end{aligned}
        #     \]
        #     ''')
        # ]
        # geometry_svm_prob_tex[1].next_to(geometry_svm_prob_tex[0], DOWN, buff=0.25).to_edge(LEFT, 1.5)
        # geometry_svm_prob = Group(geometry_svm_prob_tex[0], geometry_svm_prob_tex[1])

        # geometry_svm_draw_group.scale(0.4).next_to(geometry_svm_prob, RIGHT).to_edge(RIGHT, buff=3)

        # self.play(FadeIn(geometry_svm_prob), FadeIn(geometry_svm_draw_subgroup))
        # self.wait()
        # self.next_slide()

        # self.play(Create(geometry_svm_line))
        # self.wait()
        # self.next_slide()

        # self.play(FadeOut(geometry_pd_prob, geometry_pd_draw_group, geometry_svm_draw_group), 
        #     geometry_svm_prob.animate.next_to(subtitle_geometry, DOWN, buff=0.5).to_edge(LEFT, 1)
        # )
        # self.wait()
        # self.next_slide()
        
        # geometry_svm_bound_claim = Theorem(r'''
        #     {\bf\underline{Claim:}} Any feasible solution to SVM satisfies $s_1 \le D$, $s_2 \le D$, where $D$ is the maximum norm of the input points.
        #     ''', edge_color=BLUE)

        # self.play(FadeIn(geometry_svm_bound_claim.shift(DOWN)))
        # self.wait()
        # self.next_slide()

        # self.play(geometry_svm_bound_claim.animate.scale(0.5).to_edge(UR, buff=0.5))
        # self.wait()
        # self.next_slide()

        # geometry_svm_prob_tex[2].next_to(geometry_svm_prob_tex[0], DOWN, buff=0.25).to_edge(LEFT, 1.5)

        # self.play(FadeOut(geometry_svm_prob_tex[1]), FadeIn(geometry_svm_prob_tex[2]))
        # self.wait()
        # self.next_slide()


        # geometry_svm_ftp = [
        #     MyTex(r'''
        #         Feasibility test problem:\\
        #         Find $\mmw, s_1, s_2$ such that
        #     ''').set_color(YELLOW),
        #     MyTex(r'''
        #         \[
        #         \begin{aligned}
        #         & s_1 + s_2 \ge \hat{\alpha} \\
        #         & \mmP^T \mmw - s_1 \mmone \in \bR^{m_1}_+,  \\
        #         & -\mmQ^T \mmw - s_2 \mmone \in \bR^{m_2}_+, \\
        #         & \|\mmw\| \le 1.
        #         \end{aligned}
        #     \]'''),
        #     MyTex(r'''
        #         \[
        #         \begin{aligned}
        #         & s_1 + s_2 \ge (1 - \eps) \hat{\alpha} \\
        #         & \mmP^T \mmw - s_1 \mmone \in \bR^{m_1}_+,  \\
        #         & -\mmQ^T \mmw - s_2 \mmone \in \bR^{m_2}_+, \\
        #         & s_1 \le D,\ s_2 \le D, \\
        #         & \|\mmw\| \le 1.
        #         \end{aligned}
        #     \]''')
        # ]
        # geometry_svm_ftp[0][0][-19:].set_color(WHITE)
        # geometry_svm_ftp[0].next_to(geometry_svm_prob, RIGHT, buff=1).to_edge(UP, buff=2)
        # geometry_svm_ftp[1].next_to(geometry_svm_ftp[0], DOWN, buff=0.25).shift([geometry_svm_ftp[0].get_left()[0] - geometry_svm_ftp[1].get_left()[0] + 0.5, 0, 0])
        # geometry_svm_ftp[2].next_to(geometry_svm_ftp[0], DOWN, buff=0.25).shift([geometry_svm_ftp[0].get_left()[0] - geometry_svm_ftp[2].get_left()[0] + 0.5, 0, 0])

        # self.play(FadeIn(geometry_svm_ftp[0], geometry_svm_ftp[1]))
        # self.wait()
        # self.next_slide()

        # self.play(FadeOut(geometry_svm_ftp[1]), FadeIn(geometry_svm_ftp[2]))
        # self.wait()
        # self.next_slide()


        # geometry_svm_ftp_thm = Theorem(r'''
        #     {\bf\underline{Thm:}}
        #     There is an iterative algorithm that solves FTP in $O({D^2 \log M \over \eps^2 \hat{\alpha}^2})$ iterations, with a running time of $O(N + d)$ per iteration.
        # ''').next_to(geometry_svm_ftp[2], DOWN)
        # geometry_svm_ftp_thm.shift([-geometry_svm_ftp_thm.get_center()[0], 0, 0])

        # self.play(FadeIn(geometry_svm_ftp_thm))
        # self.wait()
        # self.next_slide()

        # self.play(geometry_svm_ftp_thm.animate.scale(0.5).next_to(geometry_svm_bound_claim, DOWN, buff=0.1).to_edge(RIGHT, buff=0.5),
        #     FadeOut(geometry_svm_prob_tex[0], geometry_svm_prob_tex[2])
        # )
        # self.play(Group(geometry_svm_ftp[0], geometry_svm_ftp[2]).animate.scale(0.8).next_to(geometry_svm_ftp_thm, DOWN, buff=0.3).to_edge(RIGHT, buff=1))
        # self.wait()
        # self.next_slide()

        # geometry_svm_ftp_proof = [
        #     MyTex(r'''\scalebox{0.85}{\parbox{10cm}{
        #     1. Reduction to zero-sum game
        #     \begin{myitemize}
        #     \item $\cc{K} = \bR^M_+$, $\displaystyle\brmf(\mmw, s_1, s_2) = \begin{pmatrix}\mmP^T \mmw - s_1 \mmone \\- \mmQ^T \mmw - s_2 \mmone\end{pmatrix}$
        #     \item $\cc{A} = \Big\{(\mmw, s_1, s_2) \in \bU : s_1 + s_2 \ge \hat{\alpha},\ s_1 \le D,\ s_2 \le D,\ \|\mmw\| \le 1 \Big\}$
        #     \item If $\hat{\alpha} \le \alpha^*$, $\displaystyle\max_{\mmx\in \cc{A}} \min_{\mmy \in \cc{B}} \ \brmf(\mmx) \bullet \mmy \ge 0$
        #     \item Solve the game up to additive error $\eps\hat{\alpha} / 2$
        #     \item If exists $t$: $\displaystyle\max_{\mmx \in \cc{A}}\ \brmf(\mmx) \bullet \xt{\mmy}{t} < 0$, then $\lambda^* < 0$ and $\hat{\alpha} > \alpha^*$
        #     \item Otherwise $(\tilde{w}, \tilde{s}_1 - {\eps\over 2}, \tilde{s}_2 - {\eps\over 2})$ is a solution to FTP
        #     \end{myitemize}
        #     }} ''', up=subtitle_geometry),
        #     MyTex(r'''\scalebox{0.85}{\parbox{10cm}{
        #     2. Implementation of {\sc Oracle}
        #     \begin{myitemize}
        #     \item $\cc{K} = \bR^M_+$, $\displaystyle\brmf(\mmw, s_1, s_2) = \begin{pmatrix}\mmP^T \mmw - s_1 \mmone \\- \mmQ^T \mmw - s_2 \mmone\end{pmatrix}$
        #     \item $\cc{A} = \Big\{(\mmw, s_1, s_2) \in \bU : s_1 + s_2 \ge \hat{\alpha},\ s_1 \le D,\ s_2 \le D,\ \|\mmw\| \le 1 \Big\}$
        #     \item If $\hat{\alpha} \le \alpha^*$, $\displaystyle\max_{\mmx\in \cc{A}} \min_{\mmy \in \cc{B}} \ \brmf(\mmx) \bullet \mmy \ge 0$
        #     \item Solve the game up to additive error $\eps\hat{\alpha} / 2$
        #     \item If exists $t$: $\displaystyle\max_{\mmx \in \cc{A}}\ \brmf(\mmx) \bullet \xt{\mmy}{t} < 0$, then $\lambda^* < 0$ and $\hat{\alpha} > \alpha^*$
        #     \item Otherwise $(\tilde{w}, \tilde{s}_1 - {\eps\over 2}, \tilde{s}_2 - {\eps\over 2})$ is a solution to FTP
        #     \end{myitemize}
        #     }} ''', up=subtitle_geometry),
        # ]

        # geometry_svm_ftp_proof[0][0][:25].set_color(RED)

        # self.play(FadeIn(geometry_svm_ftp_proof[0]))
        # self.wait()
        # self.next_slide()
        
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx




#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
# Symmetric Cone Programming ##########################################################################################

        self.play(subtitle_geometry.animate.move_to(outline_pos['subtitle_geometry']),
            FadeIn(outline_title, subtitle_eja, subtitle_game, subtitle_scp, subtitle_parallel, subtitle_conclu)
        )
        self.next_slide()
        self.play(subtitle_scp.animate.to_edge(UL, buff=0.5).set_color(WHITE),
            FadeOut(outline_title, subtitle_eja, subtitle_game, subtitle_geometry, subtitle_parallel, subtitle_conclu)
        )
        self.next_slide()

        scp_problem = [ # 0
            MyTex(r'''
            $\displaystyle
            \begin{aligned}
                \minimize\quad & \mmc^T \mmx \\
                \subto\quad & \mmA \mmx - \mmb \in \cc{K} \\
            \end{aligned}$
            ''')
        ]

        self.play(FadeIn(scp_problem[-1]))
        self.wait()
        self.next_slide()

        scp_problem.append( # 1
            MyTex(r'''
            $\displaystyle
            \begin{aligned}
                \minimize\quad & \mmc^T \mmx \\
                \subto\quad & \sum_{j=1}^m \mma_j x_j - \mmb \in \cc{K} \\
            \end{aligned}$
            ''')
        )

        self.play(FadeIn(scp_problem[-1]), FadeOut(scp_problem[-2]))
        self.wait()
        self.next_slide()

        scp_problem.append( # 2
            Text('Primal').set_font_size(25).set_color(YELLOW)
        )

        scp_problem[-1].next_to(scp_problem[-2], UP, buff=0.5)

        self.play(FadeIn(scp_problem[-1]))
        self.wait()
        self.next_slide()

        scp_problem.append( # 3
            MyTex(r'''
            $\displaystyle
            \begin{aligned}
                \maximize \quad & \mmb \bullet \mmy \\
                \subto \quad    & \mma_j \bullet \mmy = c_j,\ \forall j\in [m], \\
                                & \mmy \in \cc{K}
            \end{aligned}$
            ''')
        )
        
        scp_problem.append( # 4
            Text('Dual').set_font_size(25).set_color(YELLOW)
        )
        
        self.play(Group(scp_problem[1], scp_problem[2]).animate.shift(LEFT * 3))

        scp_problem[4].next_to(scp_problem[2], RIGHT, buff=5)
        scp_problem[3].next_to(scp_problem[4], DOWN, buff=0.5)

        self.play(FadeIn(scp_problem[3], scp_problem[4]))
        self.wait()
        self.next_slide()

        scp_problem_group = Group(scp_problem[3], scp_problem[4], scp_problem[1], scp_problem[2])

        self.play(
            scp_problem_group.animate.shift([0, subtitle_scp.get_bottom()[1] - scp_problem[4].get_top()[1] - 0.5, 0])
        )
        self.wait()
        self.next_slide()

        scp_problem_examples = [ # 0
            MyTex(r'''
            Linear program: $\cc{K} = \bR^n_+$
            ''').set_color(BLUE).next_to(scp_problem_group, DOWN, buff=0.5)
        ]

        scp_problem_examples.append( # 1
            MyTex(r'''
            $\displaystyle
            \begin{aligned}
                \min \quad       & \mmc^T \mmx \\
                {\rm s.t.} \quad & \mmA\mmx \ge \mmb \\
            \end{aligned}
            \hspace{3em}
            \begin{aligned}
                \max \quad       & \mmb^T \mmx \\
                {\rm s.t.} \quad & \mmA^T \mmy = \mmc, \\
                                & \mmy \ge 0
            \end{aligned}
            $
            ''').next_to(scp_problem_examples[-1], DOWN, buff=0.25)
        )

        self.play(FadeIn(*scp_problem_examples[-2:]))
        self.wait()
        self.next_slide()

        scp_problem_examples.append( # 2
            MyTex(r'''
            Semidefinite program: $\cc{K} = \cc{S}^n_+$
            ''').set_color(BLUE).next_to(scp_problem_group, DOWN, buff=0.5)
        )

        scp_problem_examples.append( # 3
            MyTex(r'''
            $\displaystyle
            \begin{aligned}
                \min \quad       & \mmc^T \mmx \\
                {\rm s.t.} \quad & \sum_{j=1}^m \mmA_j x_j - \mmB \in \cc{S}^n_+ \\
            \end{aligned}
            \hspace{3em}
            \begin{aligned}
                \max \quad       & \Tr(\mmB \mmY)            \\
                {\rm s.t.} \quad & \Tr(\mmA_j \mmY) = c_j, \ \forall j \in [m], \\
                                & \mmY \in \cc{S}^n_+
            \end{aligned}
            $
            ''').next_to(scp_problem_examples[-1], DOWN, buff=0.25)
        )

        self.play(FadeIn(*scp_problem_examples[-2:]), FadeOut(*scp_problem_examples[-4:-2]))
        self.wait()
        self.next_slide()

        scp_problem_examples.append( # 4
            MyTex(r'''
            Second-order cone program: $\cc{K} = \cproduct_{i=1}^n \cc{Q}^{d_i + 1}$
            ''').set_color(BLUE).next_to(scp_problem_group, DOWN, buff=0.5)
        )

        scp_problem_examples.append( # 5
            MyTex(r'''
            $\displaystyle
            \begin{aligned}
                \max \quad       & \mmc^T \mmx                                                    \\
                {\rm s.t.} \quad & \mmA_i \mmx - \mmb_i \in \cc{Q}^{d_i + 1},\ \forall i \in [n] \\
            \end{aligned}
            \hspace{2em}
            \begin{aligned}
                \min \quad       & \mmb_1^T \mmy_1 + \dots + \mmb_n^T \mmy_n           \\
                {\rm s.t.} \quad & \mmA_1^T \mmy_1 + \dots + \mmA_n^T \mmy_n = \mmc, \\
                                & \mmy_i \in \cc{Q}^{d_i + 1}, \ \forall i \in [n]
            \end{aligned}
            $
            ''').next_to(scp_problem_examples[-1], DOWN, buff=0.25)
        )

        self.play(FadeIn(*scp_problem_examples[-2:]), FadeOut(*scp_problem_examples[-4:-2]))
        self.wait()
        self.next_slide()

        scp_two_algorithms = [
            Text('Two algorithms:').set_font_size(25).set_color(RED).next_to(scp_problem_group, DOWN, buff=0.5).to_edge(LEFT, buff=1)
        ]

        scp_two_algorithms.append(
            MyTex(r'''\scalebox{0.9}{\parbox{15cm}{
            \begin{myitemize}
            \item Primal-only: find a primal-feasible $\mmx$ with $\mmc^T \mmx \le \alpha^* + \eps$
            \item Primal-dual: find a pair of solutions $\{\mmx, \mmy\}$ such that $\mmc^T \mmx \le \alpha^* + \eps$ and $\mmb \bullet \mmy \ge \alpha^* - \eps$
            \end{myitemize}
            }}''', up=scp_two_algorithms[-1]).to_edge(LEFT, buff=1)
        )
        
        self.play(FadeIn(*scp_two_algorithms), FadeOut(*scp_problem_examples[-2:]))
        self.wait()
        self.next_slide()

        scp_subtitles = [
            Text(': Primal-only').set_font_size(25).next_to(subtitle_scp, RIGHT, buff=0.1),
            Text(': Primal-dual').set_font_size(25).next_to(subtitle_scp, RIGHT, buff=0.1),
            Text(': Geometric interpretation').set_font_size(25).next_to(subtitle_scp, RIGHT, buff=0.1)
        ]

        ## Primal-only ######################################################################################################

        self.play(
            Create(scp_subtitles[0]),
            FadeOut(*scp_two_algorithms),
            FadeOut(*scp_problem[-2:])
        )

        scp_primal_assumption = MyTex(r'''
            Assumption: 
            \begin{myitemize}
            \item We have a convex $\cc{C}$ such that $\cc{C} \cap \cc{O}^* \ne \varnothing$
            \item $\cc{J} \triangleq \Big\{ j \in [m] : \lambda_{\min}(\mma_j) > 0,\ c_j > 0 \Big\} \ne \varnothing$
            \end{myitemize}
        ''', up=scp_problem[1], buff=0.5)
        scp_primal_assumption[0][:11].set_color(RED)

        self.play(
            Create(scp_primal_assumption)
        )
        self.wait()
        self.next_slide()

        scp_primal_ftp = MyTex(r'''Feasibility test problem (FTP)
            \begin{myitemize}
            \item[] Given $\hat{\alpha}$ and $\eps > 0$, find $\mmx$:
                \begin{myitemize}
                \item[] $\displaystyle
                \begin{aligned}
                & \mmc^T \mmx \le \hat{\alpha} + \eps, \\
                & \sum_{j=1}^m \mma_j x_j - \mmb \in \cc{K}
                \end{aligned}
                $
                \end{myitemize}
            \end{myitemize}
        ''').next_to(subtitle_scp, DOWN, buff=0.5).to_edge(RIGHT, buff=1)
        scp_primal_ftp[0][:27].set_color(YELLOW)
        
        self.play(Create(scp_primal_ftp))
        self.wait()
        self.next_slide()

        self.play(
            FadeOut(scp_problem[1], scp_problem[2]),
            scp_primal_ftp.animate.scale(0.9, about_point=scp_primal_ftp.get_top()).to_edge(LEFT, buff=1)
        )
        self.wait()
        self.next_slide()

        scp_primal_oracle = MyTex(r'''\scalebox{0.9}{\parbox{15cm}{
        The {\sc Oracle} problem
        \begin{myitemize}
        \item[] $\displaystyle
        \begin{aligned}
        \max_{\mmx} \quad & \sum_{j=1}^m (\mma_j \bullet \mmy)\cdot x_j - \mmb \bullet \mmy \\
        {\rm s.t.} \quad 
        & \mmc^T \mmx \le \hat{\alpha}, \\
        & \mmx \in \cc{C}
        \end{aligned}
        $
        \end{myitemize}
        }}''').next_to(subtitle_scp, DOWN, buff=0.5).to_edge(LEFT, buff=6)
        scp_primal_oracle[0][:16].set_color(YELLOW)

        self.play(Create(scp_primal_oracle))
        self.wait()
        self.next_slide()

        scp_primal_thm = Theorem(r'''
        {\bf\underline{Thm:}}
        Let $R = \min_{j\in \cc{J}} {c_j \over \lambda_{\min}(\mma_j)}$.
        There is an iterative algorithm that solves FTP using $O({R^2 \rho^2 \log r \over \eps^2})$ calls to the {\sc Oracle}.
        ''', edge_color=RED).next_to(scp_primal_assumption, DOWN, buff=0.2)
        scp_primal_thm.shift([-scp_primal_thm.get_center()[0], 0, 0])

        self.play(FadeIn(scp_primal_thm))
        self.wait()
        self.next_slide()

        self.play(
            FadeOut(scp_primal_assumption),
            scp_primal_thm.animate.scale(0.45).to_edge(UR, buff=0.5).shift([0.2, 0, 0])
        )
        self.play(scp_primal_ftp.animate.scale(0.6).next_to(scp_primal_thm, DOWN, buff=0.25).to_edge(RIGHT, 0.7))
        self.play(scp_primal_oracle.animate.scale(0.6).next_to(scp_primal_ftp, DOWN, buff=0.25).to_edge(RIGHT, 0.7))
        # self.play(scp_primal_assumption.animate.scale(0.6).next_to(scp_primal_oracle, DOWN, buff=0.25).to_edge(RIGHT, 0.7))
        self.wait()
        self.next_slide()

        scp_primal_proof = [ # 0
            MyTex(r'''\scalebox{0.9}{\parbox{15cm}{
                Reduction to zero-sum game
            }}''', up=subtitle_scp).set_color(RED)
        ]

        self.play(FadeIn(scp_primal_proof[-1]))
        self.wait()
        self.next_slide()

        scp_primal_proof.append( # 1
            MyTex(r'''\scalebox{0.9}{\parbox{15cm}{
                Let $\displaystyle \brmf(\mmx) = \sum_{j=1}^m \mma_j x_j - \mmb$
            }}''', up=scp_primal_proof[-1], buff=0.25)
        )

        self.play(FadeIn(scp_primal_proof[-1]))
        self.wait()
        self.next_slide()

        scp_primal_proof.append( # 2
            MyTex(r'''\scalebox{0.9}{\parbox{15cm}{
                If $\brmf(\mmx)\in \cc{K}$, then $\displaystyle \brmf(\mmx) \bullet \mmy \ge 0,\ \forall \mmy \in \cc{B} \subseteq \cc{K}$
            }}''', up=scp_primal_proof[-1], buff=0.25)
        )

        self.play(FadeIn(scp_primal_proof[-1]))
        self.wait()
        self.next_slide()

        scp_primal_proof.append( # 3
            MyTex(r'''\scalebox{0.9}{\parbox{15cm}{
                Let $\displaystyle \cc{A} = \Big\{\mmx \in \bR^m : \mmx \in \cc{C}, \ \mmc^T \mmx \ge \hat{\alpha} \Big\}$
            }}''', up=scp_primal_proof[-1], buff=0.25)
        )

        self.play(FadeIn(scp_primal_proof[-1]))
        self.wait()
        self.next_slide()

        scp_primal_proof.append( # 4
            MyTex(r'''\scalebox{0.9}{\parbox{15cm}{
            \begin{myitemize}
            \item If $\hat{\alpha} \ge \alpha^*$, then $\displaystyle \max_{\mmx \in \cc{A}} \min_{\mmy\in \cc{B}}\ \brmf(\mmx) \bullet \mmy = \lambda^* \ge 0$
            \end{myitemize}
            }}''', up=scp_primal_proof[-1], buff=0.25)
        )

        self.play(FadeIn(scp_primal_proof[-1]))
        self.wait()
        self.next_slide()

        scp_primal_proof.append( # 5
            MyTex(r'''\scalebox{0.9}{\parbox{15cm}{
            \begin{myitemize}
            \item If $\lambda^* < 0$, then $\cc{O}^* \cap \cc{A} = \varnothing$ and $\hat{\alpha} < \alpha^*$
            \end{myitemize}
            }}''', up=scp_primal_proof[-1], buff=0.25)
        )

        self.play(FadeIn(scp_primal_proof[-1]))
        self.wait()
        self.next_slide()

        scp_primal_proof.append( # 6
            MyTex(r'''\scalebox{0.9}{\parbox{15cm}{
                Solve the game up to an additive error ${\eps \over R}$:
            }}''', up=scp_primal_proof[0], buff=0.25)
        )

        self.play(FadeIn(scp_primal_proof[-1]), FadeOut(*scp_primal_proof[1:-1]))
        self.wait()
        self.next_slide()

        scp_primal_proof.append( # 7
            MyTex(r'''\scalebox{0.9}{\parbox{15cm}{
            \begin{myitemize}
            \item If exists $t$: $\displaystyle \max_{\mmx\in \cc{A}}\ \brmf(\mmx)\bullet \xt{\mmy}{t} < 0$, then $\lambda^* < 0$ and $\hat{\alpha} < \alpha^*$
            \end{myitemize}
            }}''', up=scp_primal_proof[-1], buff=0.25)
        )

        self.play(FadeIn(scp_primal_proof[-1]))
        self.wait()
        self.next_slide()

        scp_primal_proof.append( # 8
            MyTex(r'''\scalebox{0.9}{\parbox{15cm}{
            \begin{myitemize}
            \item If $\displaystyle \brmf(\xt{\mmx}{t})\bullet \xt{\mmy}{t} \ge 0$ for all $t = 1, \dots, T$:
            \end{myitemize}
            }}''', up=scp_primal_proof[-1], buff=0.25)
        )

        self.play(FadeIn(scp_primal_proof[-1]))
        self.wait()
        self.next_slide()

        scp_primal_proof.append( # 9
            MyTex(r'''\scalebox{0.9}{\parbox{15cm}{
            \begin{myitemize}
            \item[$\blacktriangleright$] $\displaystyle 0 \le {1\over T} \sum_{t=1}^T \brmf(\xt{\mmx}{t})\bullet \xt{\mmy}{t}$
            \end{myitemize}
            }}''', up=scp_primal_proof[-1], buff=0.25).shift([0.5, 0, 0])
        )

        self.play(FadeIn(scp_primal_proof[-1]))
        self.wait()
        self.next_slide()

        scp_primal_proof.append( # 10
            MyTex(r'''\scalebox{0.9}{\parbox{15cm}{
            \begin{myitemize}
            \item[$\blacktriangleright$] $\displaystyle 0 \le {1\over T} \sum_{t=1}^T \brmf(\xt{\mmx}{t})\bullet \xt{\mmy}{t} \le \lambda_{\min}\big(\brmf(\tilde{\mmx}) \big) + {\eps\over R}$
            \end{myitemize}
            }}''', up=scp_primal_proof[-2], buff=0.25).shift([0.5, 0, 0])
        )

        self.play(FadeIn(scp_primal_proof[-1]), FadeOut(scp_primal_proof[-2]))
        self.wait()
        self.next_slide()

        scp_primal_proof.append( # 11
            MyTex(r'''\scalebox{0.9}{\parbox{15cm}{
            \begin{myitemize}
            \item[$\blacktriangleright$] $\displaystyle 0 \le \lambda_{\min}\big(\brmf(\tilde{\mmx}) \big) + {\eps\over R}$
            \end{myitemize}
            }}''', up=scp_primal_proof[-3], buff=0.25).shift([0.5, 0, 0])
        )

        self.play(FadeIn(scp_primal_proof[-1]), FadeOut(scp_primal_proof[-2]))
        self.wait()
        self.next_slide()

        scp_primal_proof.append( # 12
            MyTex(r'''\scalebox{0.9}{\parbox{15cm}{
            \begin{myitemize}
            \item[$\blacktriangleright$] $\displaystyle \sum_{j=1}^m \tilde{x}_j \mma_j - \mmb + {\eps\over R} \mme \in \cc{K}$
            \end{myitemize}
            }}''', up=scp_primal_proof[-4], buff=0.25).shift([0.5, 0, 0])
        )

        self.play(FadeIn(scp_primal_proof[-1]), FadeOut(scp_primal_proof[-2]))
        self.wait()
        self.next_slide()

        scp_primal_proof.append( # 13
            MyTex(r'''\scalebox{0.9}{\parbox{15cm}{
            \begin{myitemize}
            \item[$\blacktriangleright$] Let $\displaystyle j^* = \argmin_{j\in \cc{J}} {c_j \over \lambda_{\min}(\mma_j)}$ and $\displaystyle \hat{\mmx} = \tilde{\mmx} + {\eps\over c_{j^*}} \mme_{j^*}$:
            \end{myitemize}
            }}''', up=scp_primal_proof[-1], buff=0.25).shift([0.5, 0, 0])
        )

        self.play(FadeIn(scp_primal_proof[-1]))
        self.wait()
        self.next_slide()

        scp_primal_proof.append( # 14
            MyTex(r'''\scalebox{0.9}{\parbox{15cm}{
            \begin{myitemize}
            \item[$\vartriangleright$] $\mmc^T \hat{\mmx} = \mmc^T \tilde{\mmx} + \eps \le \hat{\alpha} + \eps$
            \end{myitemize}
            }}''', up=scp_primal_proof[-1], buff=0.25).shift([1, 0, 0])
        )

        self.play(FadeIn(scp_primal_proof[-1]))
        self.wait()
        self.next_slide()

        scp_primal_proof.append( # 15
            MyTex(r'''\scalebox{0.9}{\parbox{15cm}{
            \begin{myitemize}
            \item[$\vartriangleright$] $\displaystyle \sum_{j=1}^m \mma_j \hat{x}_j - \mmb = \sum_{j=1}^m \mma_j \tilde{x}_j - \mmb + {\eps\over c_{j^*}} \mma_{j^*}$
            \end{myitemize}
            }}''', up=scp_primal_proof[-1], buff=0.25).shift([1, 0, 0])
        )

        self.play(FadeIn(scp_primal_proof[-1]))
        self.wait()
        self.next_slide()

        scp_primal_proof.append( # 16
            MyTex(r'''\scalebox{0.9}{\parbox{15cm}{
            \begin{myitemize}
            \item[$\vartriangleright$] $\displaystyle \sum_{j=1}^m \mma_j \hat{x}_j - \mmb = \sum_{j=1}^m \mma_j \tilde{x}_j - \mmb + {\eps\over c_{j^*}} \mma_{j^*} 
            \succeq_{\cc{K}} \sum_{j=1}^m \tilde{x}_j \mma_j - \mmb + {\eps\over R} \mme
            $
            \end{myitemize}
            }}''', up=scp_primal_proof[-2], buff=0.25).shift([1, 0, 0])
        )

        self.play(FadeIn(scp_primal_proof[-1]), FadeOut(scp_primal_proof[-2]))
        self.wait()
        self.next_slide()

        scp_primal_proof.append( # 17
            MyTex(r'''\scalebox{0.9}{\parbox{15cm}{
            \begin{myitemize}
            \item[$\vartriangleright$] $\displaystyle \sum_{j=1}^m \mma_j \hat{x}_j - \mmb = \sum_{j=1}^m \mma_j \tilde{x}_j - \mmb + {\eps\over c_{j^*}} \mma_{j^*} 
            \succeq_{\cc{K}} \sum_{j=1}^m \tilde{x}_j \mma_j - \mmb + {\eps\over R} \mme \in \cc{K}
            $
            \end{myitemize}
            }}''', up=scp_primal_proof[-3], buff=0.25).shift([1, 0, 0])
        )

        self.play(FadeIn(scp_primal_proof[-1]), FadeOut(scp_primal_proof[-2]))
        self.wait()
        self.next_slide()

        scp_primal_proof.append( # 18
            MyTex(r'''\scalebox{0.9}{\parbox{15cm}{
            \begin{myitemize}
            \item[$\vartriangleright$] $\displaystyle \sum_{j=1}^m \mma_j \hat{x}_j - \mmb \in \cc{K}
            $
            \end{myitemize}
            }}''', up=scp_primal_proof[-4], buff=0.25).shift([1, 0, 0])
        )

        self.play(FadeIn(scp_primal_proof[-1]), FadeOut(scp_primal_proof[-2]))
        self.wait()
        self.next_slide()

        self.play(FadeOut(
            scp_primal_proof[18],
            *scp_primal_proof[12:15],
            *scp_primal_proof[6:9],
            scp_primal_proof[0],
            scp_primal_thm,
            scp_primal_ftp,
            scp_primal_oracle,
            scp_subtitles[0]
        ))
        self.wait()
        self.next_slide()

        ## Primal-dual ######################################################################################################

        self.remove(*scp_problem[1:5], *scp_two_algorithms) # remove this later

        self.play(Create(scp_subtitles[1].shift([0, 0.03, 0])))
        self.wait()
        self.next_slide()

        self.play(FadeIn(*scp_problem[1:5]))
        self.wait()
        self.next_slide()

        scp_problem.append( # 5
            MyTex(r'''
            $\displaystyle
            \begin{aligned}
                \minimize\quad & \mmc^T \mmx \\
                \subto\quad 
                & \sum_{j=1}^m \mma_j x_j - \mmb \in \cc{K} \\
                & \sum_{j=1}^m \mma_j' x_j - \mmb' \in \cc{K}' \\
            \end{aligned}$
            ''').next_to(scp_problem[2], DOWN, buff=0.5)
        )

        scp_problem.append( # 6
            MyTex(r'''
            $\displaystyle
            \begin{aligned}
                \maximize \quad & \mmb \bullet \mmy + \mmb' \bdiamond \mmy' \\
                \subto \quad    & \mma_j \bullet \mmy + \mma_j' \bdiamond \mmy' = c_j,\ \forall j\in [m], \\
                                & \mmy \in \cc{K},\ \mmy' \in \cc{K}'
            \end{aligned}$
            ''').next_to(scp_problem[4], DOWN, buff=0.5).shift([0.25, 0, 0])
        )

        self.play(
            FadeOut(scp_problem[1], scp_problem[3]),
            FadeIn(scp_problem[-1], scp_problem[-2])    
        )
        self.wait()
        self.next_slide()

        scp_primal_dual_problem_group = Group(
            scp_problem[-1], scp_problem[-2], scp_problem[2], scp_problem[4]
        )

        self.play(scp_primal_dual_problem_group.animate.scale(0.7, about_point=scp_primal_dual_problem_group.get_top()))

        scp_primal_dual_example = MyTex(r'''
        A simple example:
        \begin{myitemize}
        \item Let $\mma_j' = \mme_j,\ \mmb' = 0\ \text{and}\ \cc{K}' = \bR^m_+$:
        \item[] $\displaystyle
        \hspace{3em}
        \begin{aligned}
            \min \quad & \mmc^T \mmx \\
            {\rm s.t.} \quad & \sum_{j=1}^m \mma_j x_j - \mmb \in \cc{K}, \\
             & \mmx \ge 0
        \end{aligned}
        \hspace{2em}
        \begin{aligned}
            \max \quad & \mmb \bullet \mmy \\
            {\rm s.t.} \quad & \mma_j \bullet \mmy \le c_j,\ \forall j\in [m], \\
             & \mmy \in \cc{K}
        \end{aligned}$
        \end{myitemize}
        ''').scale(0.9).next_to(scp_primal_dual_problem_group, DOWN, buff=0.5).shift([-0.3, 0, 0])
        scp_primal_dual_example[0][:15].set_color(BLUE)

        self.play(FadeIn(scp_primal_dual_example))
        self.wait()
        self.next_slide()

        scp_primal_dual_claim = Theorem(r'''
            {\bf\underline{Claim:}}
            If the index set $\cc{J} \triangleq \Big\{ j \in [m] : \lambda_{\min}(\mma_j) > 0,\ \lambda_{\min}(\mma_j') \ge 0 \Big\} \ne \varnothing$, let $R = \min_{j\in \cc{J}} {c_j \over  \lambda_{\min}(\mma_j)}$, there is an algorithm that solve the primal FTP in $O({R^2 \rho^2 \log r \over \eps^2})$ iterations.
        ''', edge_color=BLUE).next_to(scp_primal_dual_problem_group, DOWN, buff=0.5)
        scp_primal_dual_claim.shift([-scp_primal_dual_claim.get_center()[0], 0, 0])

        self.play(FadeIn(scp_primal_dual_claim), FadeOut(scp_primal_dual_example))
        self.wait()
        self.next_slide()

        scp_primal_dual_claim_proof = MyTex(r'''
            Just let $\cc{C} = \Big\{\mmx : \sum_{j=1}^m \mma_j' x_j - \mmb' \in \cc{K}' \Big\}$
        ''').set_color(BLUE).next_to(scp_primal_dual_claim, DOWN, buff=0.25)

        self.play(FadeIn(scp_primal_dual_claim_proof))
        self.wait()
        self.next_slide()

        self.play(
            FadeOut(scp_primal_dual_claim_proof),
            scp_primal_dual_claim.animate.scale(0.45).to_edge(UR, buff=0.5).shift([0.2, 0, 0])
        )
        self.play(
            scp_primal_dual_problem_group.animate.scale(0.65).next_to(scp_primal_dual_claim, DOWN, buff=0.2).to_edge(RIGHT, buff=0.4)
        )
        self.wait()
        self.next_slide()

        scp_primal_dual_proof = [ # 0
            MyTex(r'''\scalebox{0.8}{\parbox{15cm}{
                Let $\displaystyle \brmf(\mmx) = \sum_{j=1}^m \mma_j x_j - \mmb$\\
                $\displaystyle \cc{A} = \Big\{ \mmx : \sum_{j=1}^m \mma_j' x_j - \mmb' \in \cc{K}', \ \mmc^T \mmx \le \hat{\alpha} \Big\}$
            }}''', up=subtitle_scp)
        ]

        self.play(FadeIn(scp_primal_dual_proof[-1]))
        self.wait()
        self.next_slide()

        scp_primal_dual_claim2 = Theorem(r'''
            {\bf\underline{Claim:}}
            If there exists $\xt{\mmy}{t}\in \cc{K}$ such that $\displaystyle \max_{\mmx\in \cc{A}}\ \brmf(\mmx) \bullet \xt{\mmy}{t} < 0$, we can construct a dual solution with objective $> \hat{\alpha}$.
        ''').shift([0,-1,0])

        self.play(FadeIn(scp_primal_dual_claim2))
        self.wait()
        self.next_slide()

        self.play(scp_primal_dual_claim2.animate.scale(0.45).next_to(scp_primal_dual_claim, DOWN, buff=0.1))
        self.play(
            scp_primal_dual_problem_group.animate.next_to(scp_primal_dual_claim2, DOWN, buff=0.2).to_edge(RIGHT, buff=0.4)
        )

        self.wait()
        self.next_slide()

        scp_primal_dual_proof.append( # 1
            MyTex(r'''\scalebox{0.8}{\parbox{15cm}{
                Construction of dual solution
            }}''', up=scp_primal_dual_proof[-1], buff=0.25).set_color(RED)
        )

        self.play(FadeIn(scp_primal_dual_proof[-1]))
        self.wait()
        self.next_slide()

        scp_primal_dual_proof.append( # 2
            MyTex(r'''\scalebox{0.8}{\parbox{15cm}{
            The value of the following problem is less than 0:
            \begin{myitemize}
            \item[] $\displaystyle
            \begin{aligned}
                \max_{\mmx} \quad & \sum_{j=1}^m (\mma_j \bullet \xt{\mmy}{t})\cdot x_j - \mmb \bullet \xt{\mmy}{t} \\
                {\rm s.t.} \quad 
                & \mmc^T \mmx \le \hat{\alpha}, \\
                & \sum_{j=1}^m \mma_j' x_j - \mmb' \in \cc{K}'
            \end{aligned}
            $
            \end{myitemize}
            }}''', up=scp_primal_dual_proof[-1], buff=0.25)
        )

        self.play(FadeIn(scp_primal_dual_proof[-1]))
        self.wait()
        self.next_slide()

        scp_primal_dual_proof.append( # 3
            MyTex(r'''\scalebox{0.8}{\parbox{15cm}{
            The value of the following problem is greater than $\hat{\alpha}$:
            \begin{myitemize}
            \item[] $\displaystyle
            \begin{aligned}
                \min_{\mmx} \quad 
                & \mmc^T \mmx \\
                {\rm s.t.} \quad 
                & \sum_{j=1}^m (\mma_j \bullet \xt{\mmy}{t})\cdot x_j - \mmb \bullet \xt{\mmy}{t} \ge 0, \\
                & \sum_{j=1}^m \mma_j' x_j - \mmb' \in \cc{K}'
            \end{aligned}
            $
            \end{myitemize}
            }}''', up=scp_primal_dual_proof[-2], buff=0.25)
        )

        self.play(FadeIn(scp_primal_dual_proof[-1]), FadeOut(scp_primal_dual_proof[-2]))
        self.wait()
        self.next_slide()

        scp_primal_dual_proof.append( # 4
            MyTex(r'''\scalebox{0.8}{\parbox{15cm}{
            The value of the following problem is greater than $\hat{\alpha}$:
            \begin{myitemize}
            \item[] $\displaystyle
            \begin{aligned}
                \min_{\mmx} \quad 
                & \mmc^T \mmx \\
                {\rm s.t.} \quad 
                & \sum_{j=1}^m (\mma_j \bullet \xt{\mmy}{t})\cdot x_j - \mmb \bullet \xt{\mmy}{t} \ge 0, \\
                & \sum_{j=1}^m \mma_j' x_j - \mmb' \in \cc{K}'
            \end{aligned}
            \hspace{2.5em}
            \begin{aligned}
                \max_{z,\ \mmy'} \quad & (\mmb \bullet \xt{\mmy}{t}) \cdot z + \mmb' \bdiamond \mmy' \\
                {\rm s.t.} \quad & (\mma_j \bullet \xt{\mmy}{t})\cdot z + \mma_j' \bdiamond \mmy' = c_j, \ \forall j \in [m], \\
                & z \ge 0, \ \mmy' \in \cc{K}'.
            \end{aligned}
            $
            \end{myitemize}
            }}''', up=scp_primal_dual_proof[-3], buff=0.25)
        )

        self.play(FadeIn(scp_primal_dual_proof[-1]), FadeOut(scp_primal_dual_proof[-2]))
        self.wait()
        self.next_slide()

        scp_primal_dual_proof.append( # 5
            MyTex(r'''\scalebox{0.8}{\parbox{15cm}{
            The value of the following problem is greater than $\hat{\alpha}$:
            \begin{myitemize}
            \item[] $\displaystyle
            \begin{aligned}
                \max_{z,\ \mmy'} \quad & (\mmb \bullet \xt{\mmy}{t}) \cdot z + \mmb' \bdiamond \mmy' \\
                {\rm s.t.} \quad & (\mma_j \bullet \xt{\mmy}{t})\cdot z + \mma_j' \bdiamond \mmy' = c_j, \ \forall j \in [m], \\
                & z \ge 0, \ \mmy' \in \cc{K}'.
            \end{aligned}
            $
            \end{myitemize}
            }}''', up=scp_primal_dual_proof[-4], buff=0.25)
        )

        self.play(FadeIn(scp_primal_dual_proof[-1]), FadeOut(scp_primal_dual_proof[-2]))
        self.wait()
        self.next_slide()

        scp_primal_dual_proof.append( # 6
            MyTex(r'''\scalebox{0.8}{\parbox{15cm}{
            Let $(\hat{z}, \hat{\mmy}')$ be the solution to the above:
            \begin{myitemize}
            \item $(\hat{z}\xt{\mmy}{t}, \hat{\mmy}')$ is a dual SCP solution with objective $> \hat{\alpha}$
            \end{myitemize}
            }}''', up=scp_primal_dual_proof[-1], buff=0.5)
        )

        self.play(FadeIn(scp_primal_dual_proof[-1]))
        self.wait()
        self.next_slide()

        self.play(FadeOut(
            scp_primal_dual_proof[6],
            scp_primal_dual_proof[5],
            *scp_primal_dual_proof[:2],
            scp_primal_dual_claim,
            scp_primal_dual_claim2,
            scp_primal_dual_problem_group,
            scp_subtitles[1]
        ))
        self.wait()
        self.next_slide()

        scp_applications = [
            MyTex(r'''\scalebox{0.9}{\parbox{15cm}{
            Polytope distance (hard-margin SVM)
            \begin{itemize}
            \item[] $\displaystyle
            \begin{aligned}
                \minimize_{\mmgamma,\ \mmmu}\quad & \|\mmP\mmgamma - \mmQ\mmmu\|\\
                \subto\quad & \mmone^T \mmgamma = 1, \ \mmgamma \ge 0, \\
                & \mmone^T \mmmu = 1, \ \mmmu \ge 0
            \end{aligned}
            \hspace{3em}
            \begin{aligned}
            \maximize_{\mmw, s_1, s_2}\quad & s_1 + s_2  \\
            \subto\quad & \mmP^T \mmw - s_1 \mmone \ge 0,  \\
                        & -\mmQ^T \mmw - s_2 \mmone \ge 0, \\
                        & \|\mmw\| \le 1
            \end{aligned}
            $
            \end{itemize}
            }}''', up=subtitle_scp)
        ]

        scp_applications[-1][0][:32].set_color(BLUE)

        self.play(FadeIn(scp_applications[-1]))
        self.wait()
        self.next_slide()

        scp_applications.append(
            MyTex(r'''\scalebox{0.9}{\parbox{15cm}{
            Polytope distance (hard-margin SVM)
            \begin{itemize}
            \item[] $\displaystyle
            \begin{aligned}
                \minimize_{\mmgamma, \mmmu, \mm{\delta}, \delta_0} \quad & \delta_0 \\
                \subto \quad & -\mmP\mmgamma + \mmQ\mmmu - \mm{\delta} = \mmzero, \\
                & \mmone^T \mmgamma = 1,\ \mmgamma\in \bR^{m_1}_+, \\
                & \mmone^T \mmmu = 1,\ \mmmu \in \bR^{m_2}_+, \\
                & (\mm{\delta}, \delta_0) \in \cc{Q}^{d+1}
            \end{aligned}
            \hspace{3em}
            \begin{aligned}
            \maximize_{\mmw, s_1, s_2} \quad & (\mmzero, 1, 1)^T (\mmw, s_1, s_2) \\
            \subto \quad & \mmP^T \mmw - s_1 \mmone \in \bR^{m_1}_+, \\
            & -\mmQ^T \mmw - s_2 \mmone \in \bR^{m_2}_+, \\
            & (\mmw, 0) + (\mmzero, 1) \in \cc{Q}^{d+1}
            \end{aligned}
            $
            \end{itemize}
            }}''', up=subtitle_scp)
        )

        scp_applications[-1][0][:32].set_color(BLUE)

        self.play(FadeIn(scp_applications[-1]), FadeOut(scp_applications[-2]))
        self.wait()
        self.next_slide()

        scp_applications.append(
            MyTex(r'''\scalebox{0.9}{\parbox{15cm}{
            Smallest enclosing ball
            \begin{itemize}
            \item[] $\displaystyle
            \begin{aligned}
                \minimize_{\mmz,\ r}\quad & r \\
                \subto \quad & \|\mmz - \mmp_i\| \le r, \ \forall i \in [n]
            \end{aligned}
            $
            \end{itemize}
            }}''', up=scp_applications[-1])
        )

        scp_applications[-1][0][:21].set_color(BLUE)

        self.play(FadeIn(scp_applications[-1]))
        self.wait()
        self.next_slide()

        scp_applications.append(
            MyTex(r'''\scalebox{0.9}{\parbox{15cm}{
            Smallest enclosing ball
            \begin{itemize}
            \item[] $\displaystyle
            \begin{aligned}
                \minimize_{\mmz,\ r} \quad & (\mmzero, 1)^T (\mmz, r) \\
                \subto \quad & \cproduct_{i=1}^n (\mmz - \mmp_i, r) \in \cproduct_{i=1}^n \cc{Q}^{d+1} \\
            \end{aligned}
            $
            \end{itemize}
            }}''', up=scp_applications[-2])
        )

        scp_applications[-1][0][:21].set_color(BLUE)

        self.play(FadeIn(scp_applications[-1]), FadeOut(scp_applications[-2]))
        self.wait()
        self.next_slide()

        self.play(FadeOut(*scp_applications[1:4:2]))




#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
# Parallel Computing ##################################################################################################

        self.play(subtitle_scp.animate.move_to(outline_pos['subtitle_scp']),
            FadeIn(outline_title, subtitle_eja, subtitle_game, subtitle_geometry, subtitle_parallel, subtitle_conclu)
        )
        self.next_slide()
        self.play(subtitle_parallel.animate.to_edge(UL, buff=0.5).set_color(WHITE),
            FadeOut(outline_title, subtitle_eja, subtitle_game, subtitle_geometry, subtitle_scp, subtitle_conclu)
        )
        self.next_slide()

        parallel_subtitles = [
            Text(': Theoretical analysis').set_font_size(25).next_to(subtitle_parallel, RIGHT, buff=0.1),
            Text(': Experimental study').set_font_size(25).next_to(subtitle_parallel, RIGHT, buff=0.1)
        ]

        self.play(Create(parallel_subtitles[0]))

        parallel_work_depth = [ # 0
            MyTex(r'''\scalebox{0.85}{\parbox{15cm}{
            The work-depth model:
            \begin{myitemize}
            \vspace{-0.25em}
            \item A computational process forms a DAG
            \vspace{-0.25em}
            \item The work is the total number of operations
            \vspace{-0.25em}
            \item The depth is the longest path in the DAG
            \end{myitemize}
            }}''', up=subtitle_parallel)
        ]

        parallel_work_depth[-1][0][:19].set_color(YELLOW)

        self.play(FadeIn(parallel_work_depth[-1]))
        self.wait()
        self.next_slide()

        parallel_work_depth.append( # 1
            MyTex(r'''\scalebox{0.85}{\parbox{15cm}{
            Parallel reduction method
            }}''', up=parallel_work_depth[-1]).set_color(YELLOW)
        )

        self.play(FadeIn(parallel_work_depth[-1]))
        self.wait()
        self.next_slide()

        parallel_work_depth.append( # 2
            ImageMobject(r'pictures/parallel/1.png').scale(0.6).next_to(parallel_work_depth[-1], DOWN, buff=0.5)
        )
        parallel_work_depth[-1].to_edge(LEFT, buff=2)

        parallel_work_depth.append( # 3
            ImageMobject(r'pictures/parallel/2.png').scale(0.6).next_to(parallel_work_depth[-1], DOWN, buff=0.5)
        )
        parallel_work_depth[-1].move_to(parallel_work_depth[-2].get_center())

        parallel_work_depth.append( # 4
            ImageMobject(r'pictures/parallel/3.png').scale(0.6).next_to(parallel_work_depth[-1], DOWN, buff=0.5)
        )
        parallel_work_depth[-1].move_to(parallel_work_depth[-2].get_center())
        
        parallel_work_depth.append( # 5
            ImageMobject(r'pictures/parallel/4.png').scale(0.6).next_to(parallel_work_depth[-1], DOWN, buff=0.5)
        )
        parallel_work_depth[-1].move_to(parallel_work_depth[-2].get_center())

        self.play(FadeIn(parallel_work_depth[-4]))
        self.wait()
        self.next_slide()

        self.play(FadeIn(parallel_work_depth[-3]), FadeOut(parallel_work_depth[-4]))
        self.wait()
        self.next_slide()

        self.play(FadeIn(parallel_work_depth[-2]), FadeOut(parallel_work_depth[-3]))
        self.wait()
        self.next_slide()

        self.play(FadeIn(parallel_work_depth[-1]), FadeOut(parallel_work_depth[-2]))
        self.wait()
        self.next_slide()

        parallel_work_depth.append( # 6
            MyTex(r'''\scalebox{0.85}{\parbox{15cm}{
            $O(n)$ work, $O(\log n)$ depth
            }}''').set_color(RED).next_to(parallel_work_depth[1], RIGHT, buff=0.5)
        )

        self.play(FadeIn(parallel_work_depth[-1]))
        self.wait()
        self.next_slide()

        self.play(FadeOut(
            parallel_work_depth[6],
            parallel_work_depth[5],
            parallel_work_depth[1],
            parallel_work_depth[0]
        ))

        parallel_table = MyTex(r'''
            \begin{table*}
            \begin{center}
            \renewcommand{\arraystretch}{1.1}
            \begin{tabular}{|c|wl{6cm}|wc{3.3cm}|wc{3.3cm}|}
            \hline
            \multicolumn{2}{|c|}{Problem} & Work & Depth \\ 
            \hline\hline
            \multicolumn{2}{|c|}{PD (Hard-SVM)} & \scalebox{.85}{$O({R^2(N+d)\log M \over \eps^2})$} & \scalebox{.85}{$O({R^2 \log(Md) \log M \over \eps^2})$} \\\hline
            \multicolumn{2}{|c|}{SEB of Balls} & \scalebox{.85}{$O({nd \log n \over \eps^2})$} & \scalebox{.85}{$O({\log (nd) \log n \over \eps^2})$} \\\hline
            \parbox[t]{2mm}{\multirow{9}{*}{\rotatebox[origin=c]{90}{SIB of}}}
            & Convex Polytopes & \scalebox{.85}{$O({R^2(N + nd) \log n \over \eps^2})$} & \scalebox{.85}{$O({R^2 \log (Md) \log n \over \eps^2})$} \\
            & ├─ PD (Hard-SVM) & \scalebox{.85}{$O({R^2(N+d) \over \eps^2})$} & \scalebox{.85}{$O({R^2 \log (Md) \over \eps^2})$} \\
            & ├─ SEB of Points (Hard-SVDD) & \scalebox{.85}{$O({nd \log n \over \eps^2})$} & \scalebox{.85}{$O({\log (nd) \log n \over \eps^2})$} \\
            & └─ Line Segments & \scalebox{.85}{$O({R^2 nd \log n \over \eps^2})$} & \scalebox{.85}{$O({R^2 \log (nd) \log n \over \eps^2})$} \\\cline{2-4}
            & Reduced Polytopes & \scalebox{.85}{$O({R^2(N + nd) \log n \over \eps^2})$} & \scalebox{.85}{$O({R^2 \log (Md) \log n \over \eps^2})$} \\
            & └─ Soft-SVM ($C$-SVM, $\nu$-SVM) & \scalebox{.85}{$O({R^2(N+d) \over \eps^2})$} & \scalebox{.85}{$O({R^2 \log (Md) \over \eps^2})$} \\\cline{2-4}
            & AABBs (Imprecise Points) & \scalebox{.85}{$O({R^2 nd \log n \over \eps^2})$} & \scalebox{.85}{$O({R^2 \log (nd) \log n \over \eps^2})$} \\\cline{2-4}
            & Balls (Imprecise Points) & \scalebox{.85}{$O({R^2 nd \log n \over \eps^2})$} & \scalebox{.85}{$O({R^2 \log (nd) \log n \over \eps^2})$} \\\cline{2-4}
            & Ellipsoids (Distributions) & \scalebox{.85}{$O(nd^\omega + {R^2 nd^2 \log n \over \eps^2})$} & \scalebox{.85}{$O(nd^\omega + {R^2 \log (nd) \log n \over \eps^2})$} \\\hline
            \multicolumn{2}{|c|}{Soft-SIB of Points (Soft-SVDD)} & \scalebox{.85}{$O({R^2 nd \log n \over \eps^2})$} & \scalebox{.85}{$O({R^2 \log (nd) \log n \over \eps^2})$} \\\hline
            \multicolumn{2}{|c|}{PD/SVM in SCP Form} & \scalebox{.85}{$O({R^2 (N + d) \log M \over \eps^2})$} & \scalebox{.85}{$O({R^2 \log(Md) \log M \over \eps^2})$} \\\hline
            \multicolumn{2}{|c|}{SEB of Points in SCP Form} & \scalebox{.85}{$O({nd \log n \over \eps^2})$} & \scalebox{.85}{$O({\log (nd) \log n \over \eps^2})$} \\\hline
            \end{tabular}
            \end{center}
            \end{table*}
        ''').scale(0.8).next_to(subtitle_parallel, DOWN, buff=0.5)
        parallel_table.shift([-parallel_table.get_center()[0], 0, 0])

        self.play(FadeIn(parallel_table))
        self.wait()
        self.next_slide()

        self.play(FadeOut(parallel_table, parallel_subtitles[0]))
        self.play(Create(parallel_subtitles[1]))
        self.wait()
        self.next_slide()

        parallel_experiment = [
            MyTex(r'''\scalebox{0.85}{\parbox{15cm}{
            Our implementation for PD/SVM and SEB:
            \begin{myitemize}
            \item PDSCP: sequential (CPU) version, implemented in C++
            \vspace{-0.4em}
            \item PDSCP-ST: parallel (GPU) version, implemented in CUDA
            \vspace{-0.4em}
            \item Some ``standard'' strategies: line search, early stopping, etc.
            \end{myitemize}
            }}''', up=subtitle_parallel)
        ]
        
        parallel_experiment[-1][0][:33].set_color(YELLOW)

        parallel_experiment[-1][0][34:40].set_color(RED)
        parallel_experiment[-1][0][80:89].set_color(RED)

        self.play(Create(parallel_experiment[-1]))
        self.wait()
        self.next_slide()

        parallel_experiment.append(
            MyTex(r'''\scalebox{0.85}{\parbox{15cm}{
            Other solvers for comparison:
            \begin{myitemize}
            \item Cplex-QP: multi-threaded IPM QP solver by IBM
            \vspace{-0.4em}
            \item Cplex-SCP: multi-threaded IPM SCP solver by IBM
            \vspace{-0.4em}
            \item Gurobi-QP: multi-threaded IPM QP solver by Gurobi
            \vspace{-0.4em}
            \item Gurobi-SCP: multi-threaded IPM SCP solver by Gurobi
            \vspace{-0.4em}
            \item CGAL: sequential simplex-based QP solver in CGAL
            \vspace{-0.4em}
            \item XXX-ST: the sequential version of XXX
            \end{myitemize}
            }}''', up=parallel_experiment[-1])
        )
        
        parallel_experiment[-1][0][:26].set_color(YELLOW)

        parallel_experiment[-1][0][27:36].set_color(RED)
        parallel_experiment[-1][0][67:77].set_color(RED)
        parallel_experiment[-1][0][109:119].set_color(RED)
        parallel_experiment[-1][0][153:164].set_color(RED)
        parallel_experiment[-1][0][199:204].set_color(RED)
        parallel_experiment[-1][0][242:249].set_color(RED)

        self.play(Create(parallel_experiment[-1]))
        self.wait()
        self.next_slide()

        parallel_experiment.append(
            MyTex(r'''\scalebox{0.85}{\parbox{15cm}{
            Hardware:
            \begin{myitemize}
            \item CPU: Intel Core i7-9700K
            \begin{myitemize}
                \vspace{-0.4em}
                \item 32GB memory, 8 cores
            \end{myitemize}
            \vspace{-0.4em}
            \item GPU: NVIDIA RTX 2080Ti
            \begin{myitemize}
                \vspace{-0.4em}
                \item 11GB memory, 4352 cores
            \end{myitemize}
            \end{myitemize}
            }}''').to_edge(RIGHT, buff=0.6).shift(DOWN)
        )

        parallel_experiment[-1][0][:9].set_color(BLUE)

        self.play(Create(parallel_experiment[-1]))
        self.wait()
        self.next_slide()
        
        inputsize_experiments = NExperiments()
        self.play(FadeOut(subtitle_parallel, *parallel_experiment, parallel_subtitles[1]))
        self.play(FadeIn(inputsize_experiments))
        self.wait()
        self.next_slide()
        self.play(FadeOut(inputsize_experiments))

        dimension_experiments = DExperiments()
        self.play(FadeIn(dimension_experiments))
        self.wait()
        self.next_slide()
        self.play(FadeIn(subtitle_parallel, parallel_subtitles[1]), FadeOut(dimension_experiments))

        parallel_error_tables = [
            Text("Average errors of PDSCP for the PD/SVM problem").set_font_size(24).set_color(YELLOW).to_edge(UP, buff=2)
        ]
        
        parallel_error_tables.append(
            MyTex(r'''
            \begin{table*}[t]
            \centering
            \resizebox{\textwidth}{!}{
            \begin{tabular}{|c | ccccccccccc|}
            \specialrule{1pt}{0.3em}{0.05em}
            Number of points & $2^{10}$ & $2^{11}$ & $2^{12}$ & $2^{13}$ & $2^{14}$ & $2^{15}$ & $2^{16}$ & $2^{17}$ & $2^{18}$ & $2^{19}$ & $2^{20}$\\
            \hline
            Average error & 0.0004 & 0.0004 & 0.0005 & 0.0005 & 0.0006 & 0.0002 & 0.0006 & 0.0006 & 0.0007 & 0.0007 & 0.0007
            \\ 
            \specialrule{1pt}{0.05em}{0.2em}
            \end{tabular}
            }
            \resizebox{.9\textwidth}{!}{
            \begin{tabular}{|c | ccccccccc|}
            \specialrule{1pt}{0em}{0.05em}
            Number of dimensions & 2 & 4 & 8 & 16 & 32 & 64 & 128 & 256 & 512\\
            \hline
            Average error & 0.0025&0.0023&0.0015&0.0011&0.0008&0.0006&0.0006&0.0006&0.0007
            \\ 
            \specialrule{1pt}{0.05em}{0em}
            \end{tabular}
            }
            \end{table*}
            ''').next_to(parallel_error_tables[-1], DOWN, buff=0.25)
        )

        parallel_error_tables.append(
            Text("Average errors of PDSCP for the SEB problem").set_font_size(24).set_color(YELLOW).next_to(parallel_error_tables[-1], DOWN, buff=0.5)
        )

        parallel_error_tables.append(
            MyTex(r'''
            \begin{table*}[t]
            \centering
            \resizebox{\textwidth}{!}{
            \begin{tabular}{|c | ccccccccccc|}
            \specialrule{1pt}{0.3em}{0.05em}
            Number of points & $2^{10}$ & $2^{11}$ & $2^{12}$ & $2^{13}$ & $2^{14}$ & $2^{15}$ & $2^{16}$ & $2^{17}$ & $2^{18}$ & $2^{19}$ & $2^{20}$\\
            \hline
            Average error & 0.0019 & 0.0021 & 0.0023 & 0.0024 & 0.0025 & 0.0029 & 0.0031 & 0.0042 & 0.0041 & 0.0044 & 0.0055\\ 
            \specialrule{1pt}{0.05em}{0.2em}
            \end{tabular}
            }
            \resizebox{.9\textwidth}{!}{
            \begin{tabular}{|c | ccccccccc|}
            \specialrule{1pt}{0em}{0.05em}
            Number of dimensions & 2 & 4 & 8 & 16 & 32 & 64 & 128 & 256 & 512\\
            \hline
            Average error & 0.0003 & 0.0009 & 0.0008 & 0.0012 & 0.0024 & 0.0027 & 0.0058 & 0.0085 & 0.0098
            \\ 
            \specialrule{1pt}{0.05em}{0em}
            \end{tabular}
            }
            \end{table*}
            ''').next_to(parallel_error_tables[-1], DOWN, buff=0.25)
        )

        self.play(FadeIn(*parallel_error_tables))
        self.wait()
        self.next_slide()

        self.play(FadeOut(*parallel_error_tables, parallel_subtitles[1]))




############################################################################################################################
############################################################################################################################
############################################################################################################################
# Conclusion ###############################################################################################################

        self.play(subtitle_parallel.animate.move_to(outline_pos['subtitle_parallel']),
            FadeIn(outline_title, subtitle_eja, subtitle_game, subtitle_geometry, subtitle_scp, subtitle_conclu)
        )
        self.next_slide()
        self.play(subtitle_conclu.animate.to_edge(UL, buff=0.5),
            FadeOut(outline_title, subtitle_eja, subtitle_game, subtitle_geometry, subtitle_scp, subtitle_parallel)
        )
        self.next_slide()

        conclusion = MyTex(r'''\scalebox{0.88}{\parbox{15cm}{
            Conclusion:
            \begin{myitemize}
            \item A new framework of zero-sum game over symmetric cones
            \vspace{-.4em}
            \item Approximation algorithms for geometric problems: PD, SEBB, SIB, Soft-SIB
            \vspace{-.4em}
            \item Two algorithms for SCP: primal-only and primal-dual
            \vspace{-.4em}
            \item Analysis and implementation of the algorithms in parallel settings
            \end{myitemize}
        }}''', up=subtitle_conclu)

        conclusion[0][:11].set_color(BLUE)

        self.play(FadeIn(conclusion))
        self.wait()
        self.next_slide()

        future_directions = MyTex(r'''\scalebox{0.88}{\parbox{15cm}{
            Future research directions:
            \begin{myitemize}
            \item Zero-sum game in EJA: Other applications? Sublinear or quantum algorithms?
            \vspace{-.4em}
            \item Geometric optimization: Lower bounds? Sublinear algos? Non-Euclidean spaces?
            \vspace{-.4em}
            \item Symmetric cone programming: Width-independent algorithms? Positive SCP?
            \vspace{-.4em}
            \item Parallel computing: Implementation for other problems (e.g.\ SIB)?
            \end{myitemize}
        }}''', up=conclusion)

        future_directions[0][:25].set_color(BLUE)

        self.play(FadeIn(future_directions))
        self.wait()
        self.next_slide()

        self.play(FadeOut(conclusion, future_directions, subtitle_conclu))




############################################################################################################################
############################################################################################################################
############################################################################################################################
# ENDING ###################################################################################################################

        self.play(FadeIn(Text("Thank you for listening!").scale(0.7)))
