from manim import *
from manim_slides import Slide, ThreeDSlide

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
        \newlist{myitemize}{itemize}{1}
        \setlist[myitemize,1]{label=\textbullet,leftmargin=10pt,itemsep=.5em}

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
    pd = ImageMobject("pictures/experiments/pd_n_100k.png").shift(UL, 1)
    seb = ImageMobject("pictures/experiments/ses_n_100k.png").next_to(pd, DOWN, buff=0.1)
    pd_text = Text("PD/SVM").rotate(PI/2).next_to(pd, LEFT).scale(0.5)
    seb_text = Text("SEB").rotate(PI/2).next_to(seb, LEFT).scale(0.5)
    group = Group(pd,seb,pd_text,seb_text).scale(0.9)
    title = Text("Different Dimensionalities").rotate(PI/2).scale(0.6).next_to(group, LEFT)
    return Group(group, title)

def NExperiments():
    pd = ImageMobject("pictures/experiments/pd_d_64.png").shift(UL, 1)
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
        # title = TitlePage()
        # self.add(title)
        # self.wait()
        # self.next_slide()
        # self.remove(title)

        # Subtitles ###################################################################################################
        subtitle_eja = Text("Euclidean Jordan Algebra & Symmetric Cones")
        subtitle_game = Text("Zero-Sum Games in EJA")
        subtitle_geometry = Text("Geometric Optimization", color=BLUE)
        subtitle_scp = Text("Symmetric Cone Programming", color=YELLOW)
        subtitle_parallel = Text("Parallel Computing", color=RED)
        subtitle_conclu = Text("Conclusion & Future Directions")

        # # Introduction ################################################################################################
        # intro_pos = {
        #     'circle_geometry' : UL * 1.2,
        #     'circle_scp' : UR * 1.2,
        #     'circle_parallel' : DOWN * 0.75 * 1.2,
        #     'subtitle_geometry' : UL * 2 + DOWN * 0.4,
        #     'subtitle_scp' : UR * 2 + DOWN * 0.4,
        #     'subtitle_parallel' : DOWN + DOWN * 0.8
        # }
        # for x in intro_pos.keys():
        #     intro_pos[x] += DOWN * 0.45

        # intro_circle_geometry = Circle(radius=2.5, color=BLUE, fill_color=BLUE, fill_opacity=0.1)
        # intro_circle_scp = Circle(radius=2.5, color=YELLOW, fill_color=YELLOW, fill_opacity=0.1)
        # intro_circle_parallel = Circle(radius=2.5, color=RED, fill_color=RED, fill_opacity=0.1)
        # intro_circle_group = Group(intro_circle_geometry, intro_circle_scp, intro_circle_parallel)

        # intro_circle_geometry.move_to(intro_pos['circle_geometry'])
        # intro_circle_scp.move_to(intro_pos['circle_scp'])
        # intro_circle_parallel.move_to(intro_pos['circle_parallel'])

        # self.play(
        #     GrowFromCenter(intro_circle_geometry),
        #     GrowFromCenter(intro_circle_scp),
        #     GrowFromCenter(intro_circle_parallel)
        # )

        # subtitle_geometry.move_to(intro_pos['subtitle_geometry']).set_font_size(25).rotate(PI / 3)
        # subtitle_scp.move_to(intro_pos['subtitle_scp']).set_font_size(22).rotate(-PI / 3)
        # subtitle_parallel.move_to(intro_pos['subtitle_parallel']).set_font_size(25)

        # intro_group = Group(intro_circle_group, subtitle_geometry, subtitle_scp, subtitle_parallel)

        # self.play(
        #     FadeIn(subtitle_geometry, subtitle_scp, subtitle_parallel)
        # )

        # self.wait()
        # self.next_slide()

        # ## Intro - Goemetric Optimization
        # self.play(Rotate(intro_group, -PI/3, about_point=(intro_circle_geometry.get_center() + intro_circle_scp.get_center() + intro_circle_parallel.get_center())/3))

        # intro_pos['circle_geometry'] = intro_circle_geometry.get_center()
        # intro_pos['circle_scp'] = intro_circle_scp.get_center()
        # intro_pos['circle_parallel'] = intro_circle_parallel.get_center()
        # intro_pos['subtitle_geometry'] = subtitle_geometry.get_center()
        # intro_pos['subtitle_scp'] = subtitle_scp.get_center()
        # intro_pos['subtitle_parallel'] = subtitle_parallel.get_center()

        # self.play(
        #     intro_circle_geometry.animate.scale(10).set_fill(None, opacity=0),
        #     subtitle_geometry.animate.set_font_size(30).to_edge(UP, buff=0.5),
        #     intro_circle_scp.animate.shift(DR * 10),
        #     subtitle_scp.animate.shift(DR * 10),
        #     intro_circle_parallel.animate.shift(DL * 10),
        #     subtitle_parallel.animate.shift(DL * 10)
        # )

        # self.next_slide()

        # ## Intro - Symmetric Cone Programming
        # self.play(
        #     intro_circle_geometry.animate.scale(1 / 10).set_fill(BLUE, opacity=0.1),
        #     subtitle_geometry.animate.set_font_size(25).move_to(intro_pos['subtitle_geometry']),
        #     intro_circle_scp.animate.move_to(intro_pos['circle_scp']),
        #     subtitle_scp.animate.move_to(intro_pos['subtitle_scp']),
        #     intro_circle_parallel.animate.move_to(intro_pos['circle_parallel']),
        #     subtitle_parallel.animate.move_to(intro_pos['subtitle_parallel'])
        # )

        # self.next_slide()

        # self.play(Rotate(intro_group, PI* 2 / 3, about_point=(intro_circle_geometry.get_center() + intro_circle_scp.get_center() + intro_circle_parallel.get_center())/3))

        # intro_pos['circle_geometry'] = intro_circle_geometry.get_center()
        # intro_pos['circle_scp'] = intro_circle_scp.get_center()
        # intro_pos['circle_parallel'] = intro_circle_parallel.get_center()
        # intro_pos['subtitle_geometry'] = subtitle_geometry.get_center()
        # intro_pos['subtitle_scp'] = subtitle_scp.get_center()
        # intro_pos['subtitle_parallel'] = subtitle_parallel.get_center()

        # self.play(
        #     intro_circle_geometry.animate.shift(DR * 10),
        #     subtitle_geometry.animate.shift(DR * 10),
        #     intro_circle_scp.animate.scale(10).set_fill(None, opacity=0),
        #     subtitle_scp.animate.set_font_size(30).to_edge(UP, buff=0.5),
        #     intro_circle_parallel.animate.shift(DL * 10),
        #     subtitle_parallel.animate.shift(DL * 10)
        # )

        # self.next_slide()

        # ## Intro - Parallel Computing
        # self.play(
        #     intro_circle_geometry.animate.move_to(intro_pos['circle_geometry']),
        #     subtitle_geometry.animate.move_to(intro_pos['subtitle_geometry']),
        #     intro_circle_scp.animate.scale(1 / 10).set_fill(YELLOW, opacity=0.1),
        #     subtitle_scp.animate.set_font_size(22).move_to(intro_pos['subtitle_scp']),
        #     intro_circle_parallel.animate.move_to(intro_pos['circle_parallel']),
        #     subtitle_parallel.animate.move_to(intro_pos['subtitle_parallel'])
        # )

        # self.next_slide()

        # self.play(Rotate(intro_group, - PI / 3, about_point=(intro_circle_geometry.get_center() + intro_circle_scp.get_center() + intro_circle_parallel.get_center())/3))

        # intro_pos['circle_geometry'] = intro_circle_geometry.get_center()
        # intro_pos['circle_scp'] = intro_circle_scp.get_center()
        # intro_pos['circle_parallel'] = intro_circle_parallel.get_center()
        # intro_pos['subtitle_geometry'] = subtitle_geometry.get_center()
        # intro_pos['subtitle_scp'] = subtitle_scp.get_center()
        # intro_pos['subtitle_parallel'] = subtitle_parallel.get_center()

        # self.play(
        #     intro_circle_geometry.animate.shift(UL * 10),
        #     subtitle_geometry.animate.shift(UL * 10),
        #     intro_circle_scp.animate.shift(UR * 10),
        #     subtitle_scp.animate.shift(UR * 10),
        #     intro_circle_parallel.animate.scale(10).set_fill(None, opacity=0),
        #     subtitle_parallel.animate.set_font_size(30).to_edge(UP, buff=0.5)
        # )

        # self.next_slide()


        # ## Intro - Ending
        # self.play(
        #     intro_circle_geometry.animate.move_to(intro_pos['circle_geometry']),
        #     subtitle_geometry.animate.move_to(intro_pos['subtitle_geometry']),
        #     intro_circle_scp.animate.move_to(intro_pos['circle_scp']),
        #     subtitle_scp.animate.move_to(intro_pos['subtitle_scp']),
        #     intro_circle_parallel.animate.scale(1 / 10).set_fill(RED, opacity=0.1),
        #     subtitle_parallel.animate.set_font_size(25).move_to(intro_pos['subtitle_parallel'])
        # )

        # self.next_slide()
        # self.play(FadeOut(intro_circle_group))

        # # Outline #####################################################################################################
        # ## Euclidean Jordan Algebra & Symmetric Cones
        # ## Zero-Sum Game in EJA
        # ## Geometric Optimization
        # ## Symmetric Cone Programming
        # ## Parallel Computing
        # ## Conclusion and Future Directions

        # self.play(
        #     subtitle_geometry.animate.rotate(-PI/3).set_font_size(25).move_to([0., 0.41891479, 0.]),
        #     subtitle_scp.animate.rotate(PI/3).set_font_size(25).move_to([0, -4.13218177e-01, 0]),
        #     subtitle_parallel.animate.move_to([0, -1.24814859e+00, 0])
        # )

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

        # self.play(FadeIn(outline_title, subtitle_eja, subtitle_game, subtitle_conclu))
        # self.wait()
        # self.next_slide()

        # # EJA & Symmetric Cones #######################################################################################

        # self.play(subtitle_eja.animate.to_edge(UL, buff=0.5),
        #     FadeOut(outline_title, subtitle_game, subtitle_geometry, subtitle_scp, subtitle_parallel, subtitle_conclu)
        # )

        # self.next_slide()

        # jordan_algebra_1 = MyTex(r'''Jordan algebra $(\bJ, \circ)$: a finite-dimensional vector space $\bJ$ 
        # and a bilinear binary operation $\circ$ satisfying:
        # \begin{enumerate}
        #     \item (Commutativity) $\mmx \circ\mmy = \mmy \circ \mmx$,
        #     \item (Jordan identity) $\mmx^2 \circ (\mmx \circ \mmy) = \mmx \circ (\mmx^2 \circ \mmy)$.
        # \end{enumerate}
        # ''', up=subtitle_eja)
        # jordan_algebra_1[0][0:19].set_color(BLUE)

        # jordan_algebra_2 = MyTex(r'''
        # Identity element: $\mmx \circ \mme = \mme \circ \mmx = \mmx$ for all $\mmx\in \bJ$
        # ''', up=jordan_algebra_1)
        # jordan_algebra_2[0][0:16].set_color(YELLOW)        

        # jordan_algebra_3 = MyTex(r'''
        # Powers: $\mmx^0 \triangleq \mme, \quad \mmx^k \triangleq \mmx\circ \mmx^{k-1},\ \forall k \ge 1$
        # ''', up=jordan_algebra_2, buff=0.3)
        # jordan_algebra_3[0][:7].set_color(YELLOW)

        # jordan_algebra_4 = MyTex(r'''
        # Degree of $\mmx$: the smallest $k\in \mathbbm{Z}_+$ such that $\mme, \mmx, \dots, \mmx^k$ are linearly dependent 
        # ''', up=jordan_algebra_3, buff=0.3)
        # jordan_algebra_4[0][:10].set_color(YELLOW)

        # jordan_algebra_5 = MyTex(r'''
        # Rank of $\bJ$: the largest degree of all $\mmx \in \bJ$
        # ''', up=jordan_algebra_4, buff=0.3)
        # jordan_algebra_5[0][:8].set_color(YELLOW)

        # self.play(FadeIn(jordan_algebra_1))
        # self.next_slide()

        # self.play(FadeIn(jordan_algebra_2, jordan_algebra_3, jordan_algebra_4, jordan_algebra_5))
        # self.next_slide()

        # self.play(FadeOut(jordan_algebra_1, jordan_algebra_2, jordan_algebra_3, jordan_algebra_4, jordan_algebra_5))

        # eja_1 = MyTex(r'''
        # Euclidean Jordan algebra $(\bJ, \circ, \bullet)$: a Jordan algebra endowed with an inner product 
        # $\bullet: \bJ \times \bJ \rightarrow \bR$ satisfying
        # \[
        # \mmx \bullet (\mmy \circ \mmz) = (\mmx \circ \mmy) \bullet \mmz, \quad \forall \mmx, \mmy, \mmz\in \bJ
        # \]
        # ''', up=subtitle_eja)
        # eja_1[0][:30].set_color(BLUE)

        # eja_2 = MyTex(r'''
        # Spectral decomposition: 
        # \[ \mmx = \sum_{k=1}^r \lambda_k(\mmx)\mmq_k, \]
        # where $\lambda_1(\mmx), \dots, \lambda_r(\mmx)\in \bR$ are eigenvalues, and $\mmq_1,\dots, \mmq_r \in \bJ$ 
        # are primitive orthogonal {\em idempotents} (or eigenvectors) satisfying:
        # \begin{enumerate}
        #     \item (Idempotents and primitiveness) $\mmq_k^2 = \mmq_k$ and $\mmq_k\bullet \mmq_k = 1$, $\forall k \in [r]$,
        #     \item (Orthogonality) $\mmq_i \circ \mmq_j = 0,\ \forall i \neq j,\ i,j\in [r]$,
        #     \item (Completeness) $\sum_{k=1}^r \mmq_k = \mme$.
        # \end{enumerate}
        # ''', up=eja_1)
        # eja_2[0][:22].set_color(YELLOW)
        # eja_2[0][62:73].set_color(RED)
        # eja_2[0][124:136].set_color(RED)

        # self.play(FadeIn(eja_1))
        # self.next_slide()

        # self.play(FadeIn(eja_2))
        # self.next_slide()

        # eja_3 = MyTex(r'''
        # Trace, determinant, and exponential:
        # \[
        #     \Tr(\mmx) \triangleq \sum_{k=1}^r \lambda_k(\mmx), \quad {\bf det}(\mmx) \triangleq \prod_{k=1}^r \lambda_k(\mmx) \quad \text{and} \quad
        #     \mmexp(\mmx) \triangleq \sum_{k=1}^r \exp(\lambda_k(\mmx))\mmq_k
        # \]
        # ''', up=subtitle_eja)
        # eja_3[0][:33].set_color(YELLOW)

        # self.play(FadeOut(eja_1, eja_2))
        # self.play(FadeIn(eja_3))
        # self.next_slide()

        # eja_4 = MyTex(r'''
        # Infinity norm: $\|\mmx\|_\infty = \max_{k} |\lambda_k(\mmx)|$
        # ''', up=eja_3)
        # eja_4[0][:12].set_color(YELLOW)

        # self.play(FadeIn(eja_4))

        # eja_5 = MyTex(r'''
        # Trace inner product: $\mmx\bullet \mmy = \Tr(\mmx \circ \mmy)$
        # ''', up=eja_4)
        # eja_5[0][:18].set_color(YELLOW)

        # self.play(FadeIn(eja_5))

        # eja_6 = MyTex(r'''
        # Golden-Thompson inequality: 
        # \[\Tr(\mmexp(\mmx + \mmy)) \le \Tr(\mmexp(\mmx)\circ\mmexp(\mmy)) = \mmexp(\mmx)\bullet \mmexp(\mmy)\]
        # ''', up=eja_5)
        # eja_6[0][:26].set_color(YELLOW)

        # self.play(FadeIn(eja_6))
        # self.next_slide()

        # self.play(FadeOut(eja_3, eja_4, eja_5, eja_6))

        # sc_1 = MyTex(r'''
        # Symmetric cones are convex cones that are {\em self-dual} and {\em homogeneous}:
        # \begin{itemize}
        # \item $\cc{K} = \cc{K}^*$, where $\cc{K}^* = \big\{\mmy \in \bJ : \forall \mmx \in \cc{K},\ \mmx \bullet \mmy\ge 0 \big\}$
        # \item There exists invertible operators $\cc{T}$ such that $\cc{T}(\cc{K}) = \cc{K}$
        # \end{itemize}
        # ''', up=subtitle_eja)
        # sc_1[0][:14].set_color(BLUE)
        # sc_1[0][35:44].set_color(RED)
        # sc_1[0][47:58].set_color(RED)
        # sc_1[0][60:64].set_color(RED)
        # sc_1[0][-6:].set_color(RED)

        # self.play(FadeIn(sc_1))
        # self.next_slide()

        # sc_2 = MyTex(r'''
        # Jordan algebraic characterization of symmetric cones: 
        # \begin{itemize}
        # \item (Cone of squares) $\cc{K} = \big\{\mmx^2 : \mmx \in \bJ \big\}$
        # \item (Cone of positivity) $\cc{K}^* = \big\{\mmy \in \bJ : \forall \mmx \in \cc{K},\ \mmx \bullet \mmy\ge 0 \big\}$
        # \end{itemize}
        # ''', up=sc_1)
        # sc_2[0][:31].set_color(BLUE)
        # sc_2[0][49:64].set_color(YELLOW)
        # sc_2[0][75:93].set_color(YELLOW)

        # self.play(FadeIn(sc_2))
        # self.next_slide()

        # sc_3 = MyTex(r'''
        # Examples of symmetric cones: nonnegative orthant $\bR^n_+$, cone of real symmetric 
        # PSD matrices $\cc{S}^n_+$, second-order cones $\cc{Q}^{d+1}$, and their Cartesian products
        # ''', up=sc_2)
        # sc_3[0][:25].set_color(BLUE)
        # sc_3[0][43:46].set_color(YELLOW)
        # sc_3[0][77:80].set_color(YELLOW)
        # sc_3[0][98:102].set_color(YELLOW)
        # sc_3[0][-17:].set_color(YELLOW)
        
        # self.play(FadeIn(sc_3))
        # self.next_slide()

        # self.play(FadeOut(sc_1, sc_2, sc_3))

        # sc_4 = MyTex(r'''
        # Nonnegative orthant $\bR^n_+$:
        # \begin{myitemize}
        # \item[] Space: $\bJ = \bR^n$ \hspace{2em}
        # Jordan product: $\mmx \circ \mmy = \diag(\mmx) \mmy$\\
        # \vspace{-1.3em}
        # \item[] Identity: $\mme = \mmone_n$ \hspace{1em}
        # Trace: $\Tr(\mmx) = \sum_k x_k$ \hspace{1em}
        # Inner product: $\mmx \bullet \mmy = \mmx^T \mmy$\\
        # \vspace{-1.3em}
        # \item[] Spectral decomposition: $\eigenval{k}{\mmx} = x_k,\ \mmq_k = \mme_k$\\
        # \end{myitemize}
        # ''', up=subtitle_eja)
        # sc_4[0][:22].set_color(BLUE)
        # sc_4[0][22:28].set_color(YELLOW)
        # sc_4[0][32:46].set_color(YELLOW)
        # sc_4[0][58:67].set_color(YELLOW)
        # sc_4[0][116-45:122-45].set_color(YELLOW)
        # sc_4[0][132-45:145-45].set_color(YELLOW)
        # sc_4[0][80+27:102+27].set_color(YELLOW)

        # self.play(FadeIn(sc_4))
        # self.next_slide()

        # sc_5 = MyTex(r'''
        # PSD cone $\cc{S}^n_+$:
        # \begin{myitemize}
        # \item[] Space: $\bJ = \bR^{n^2}$ \hspace{2em}
        # Jordan product: $\mmx \circ\mmy = {1\over 2} \vecc(\mmX\mmY + \mmY\mmX)$\\
        # \vspace{-1.3em}
        # \item[] Identity: $\mme = \vecc(\mmI)$ \hspace{1em}
        # Trace: $\Tr(\mmx) = \Tr(\mmX)$ \hspace{1em}
        # Inner product: $\mmx \bullet \mmy = \mmx^T \mmy$\\
        # \vspace{-1.3em}
        # \item[] Spectral decomposition: $\eigenval{k}{\mmx} = \eigenval{k}{\mmX},\ \mmq_k = \vecc(\mmv_k\mmv_k^T)$\\
        # \end{myitemize}
        # ''', up=sc_4)
        # sc_5[0][:11].set_color(BLUE)
        # sc_5[0][11:17].set_color(YELLOW)
        # sc_5[0][22:36].set_color(YELLOW)
        # sc_5[0][53:62].set_color(YELLOW)
        # sc_5[0][117-47:123-47].set_color(YELLOW)
        # sc_5[0][134-47:147-47].set_color(YELLOW)
        # sc_5[0][70+37:92+37].set_color(YELLOW)

        # self.play(FadeIn(sc_5))
        # self.next_slide()

        # self.play(FadeOut(sc_4, sc_5))

        # sc_6 = MyTex(r'''
        # Second-order cone $\cc{Q}^{d+1}$: $\quad \mmx = (\bar{\mmx}, x_0),\ \mmy = (\bar{\mmy}, y_0)$
        # \begin{myitemize}
        # \item[] Space: $\bJ = \bR^{d}\times \bR$ \hspace{2em}
        # Jordan product: $\mmx \circ \mmy = {1\over \sqrt{2}}(x_0\bar{\mmy} + y_0\bar{\mmx},\ \mmx^T \mmy)$\\
        # \vspace{-1.3em}
        # \item[] Identity: $\mme = (\mmzero, \sqrt{2})$ \hspace{1em}
        # Trace: $\Tr(\mmx) = \sqrt{2} x_0$ \hspace{1em}
        # Inner product: $\mmx \bullet \mmy = \mmx^T \mmy$\\
        # \vspace{-1.3em}
        # \item[] Spectral decomposition: $\eigenval{1,2}{\mmx} = {1\over\sqrt{2}} (x_0 \pm \|\bar{\mmx}\|),\ \mmq_{1,2} = {1\over \sqrt{2}} (\pm \mmu, 1)$\\
        # \end{myitemize}
        # ''', up=subtitle_eja)
        # sc_6[0][:21].set_color(BLUE)
        # sc_6[0][11+29:17+29].set_color(YELLOW)
        # sc_6[0][22+30:36+30].set_color(YELLOW)
        # sc_6[0][53+37:62+37].set_color(YELLOW)
        # sc_6[0][117-9:123-9].set_color(YELLOW)
        # sc_6[0][134-9:147-9].set_color(YELLOW)
        # sc_6[0][70+75:92+75].set_color(YELLOW)

        # self.play(FadeIn(sc_6))
        # self.next_slide()

        # sc_7 = MyTex(r'''
        # Product cone $\cc{K}_1\times \dots \times \cc{K}_n$: $\quad \mmx = \cproduct_{i=1}^n \mmx_i = (\mmx_1, \dots, \mmx_n)$
        # \begin{myitemize}
        # \item[] Space: $\bJ = \bJ_1 \times \dots \times \bJ_n$ \hspace{2em}
        # Jordan product: $\mmx \circ \mmy = \cproduct_{i=1}^n (\mmx_i \circ \mmy_i)$\\
        # \vspace{-1.3em}
        # \item[] Identity, trace, inner product: concatenation/sum of those of sub-EJAs\\
        # \vspace{-1.3em}
        # \item[] Spectral decomposition: follows from the decompositions of sub-EJAs\\
        # \end{myitemize}
        # ''', up=sc_6)
        # sc_7[0][:21].set_color(BLUE)
        # sc_7[0][11+31:17+31].set_color(YELLOW)
        # sc_7[0][22+37:36+37].set_color(YELLOW)
        # sc_7[0][53+36:62+55].set_color(YELLOW)
        # sc_7[0][70+81:92+81].set_color(YELLOW)

        # self.play(FadeIn(sc_7))
        # self.next_slide()
        
        # self.play(FadeOut(sc_6, sc_7))

        # # Zero-Sum Game ###############################################################################################

        # self.play(subtitle_eja.animate.move_to(outline_pos['subtitle_eja']),
        #     FadeIn(outline_title, subtitle_game, subtitle_geometry, subtitle_scp, subtitle_parallel, subtitle_conclu)
        # )
        # self.next_slide()
        # self.play(subtitle_game.animate.to_edge(UL, buff=0.5),
        #     FadeOut(outline_title, subtitle_eja, subtitle_geometry, subtitle_scp, subtitle_parallel, subtitle_conclu)
        # )
        # self.next_slide()

        # game_circle_2 = Circle(radius=0.8, fill_color=RED, fill_opacity=0.2).stretch_to_fit_height(3.5).rotate(-PI/5).stretch_to_fit_height(3.5).shift(UP * 0.5)
        # game_circle_1 = Circle(radius=1.3, fill_color=RED, fill_opacity=0.2).stretch_to_fit_height(3.5).next_to(game_circle_2, LEFT, buff=1.5)
        # game_polygon = Polygon([0, 0, 0], [-1, 2, 0], [1, 4, 0], [5, 4, 0], [4, 0.5, 0], color=YELLOW, fill_color=YELLOW, fill_opacity=0.2).scale(0.5).stretch_to_fit_height(3.5).next_to(game_circle_2, RIGHT, buff=1.5)

        # game_alice = Text("Alice", color=RED).scale(0.6).next_to(game_circle_1, UP)
        # game_bob = Text("Bob", color=YELLOW).scale(0.6).next_to(game_polygon, UP)

        # game_circle_1_text = MyTex(r'$\cc{A}\subseteq \bU$').set_color(RED).scale(0.8).move_to(game_circle_1.get_center())
        # game_circle_2_text = MyTex(r'$\brmf(\cc{A})\subseteq \bJ$').set_color(RED).scale(0.8).move_to(game_circle_2.get_center())
        # game_polygon_text = MyTex(r'\[\begin{gathered}\cc{B}=\big\{\mmy \in \cc{K}: \Tr(\mmy) = 1 \big\}\\ \subseteq \bJ \end{gathered}\]').set_color(YELLOW).scale(0.8).rotate(PI/3).move_to(game_polygon.get_center())

        # self.play(FadeIn(game_circle_1, game_polygon, game_alice, game_bob, game_circle_1_text, game_polygon_text))

        # self.next_slide()

        # alice_point = Dot(game_circle_1.get_center(), radius=0.05, color=WHITE).shift(RIGHT * 0.5 + UP * 1)
        # alice_point_label = MyTex(r'$\mmx$').next_to(alice_point, UL, buff=0.05)
        # bob_point = Dot(game_polygon.get_center(), radius=0.05, color=WHITE).shift(LEFT * 0.6 + UP * 0.7)
        # bob_point_label = MyTex(r'$\mmy$').next_to(bob_point, UR, buff=0.05)
        
        # self.play(FadeIn(alice_point, alice_point_label, bob_point, bob_point_label))

        # self.next_slide()
        
        # alice_point_2 = Dot(game_circle_2.get_center(), radius=0.05, color=WHITE).shift(RIGHT * 0.5 + UP * 1)
        # alice_point_2_label = MyTex(r'$\brmf(\mmx)$').next_to(alice_point_2, DOWN, buff=0.1)
        # alice_trans_arrow = Arrow(alice_point, alice_point_2, buff=0.1, stroke_width=4, max_tip_length_to_length_ratio=0.05)
        # alice_trans_text = MyTex(r'$\brmf : \bU \rightarrow \bJ$').scale(0.9).rotate(-PI/120).next_to(alice_trans_arrow, UP, buff=0.1)
        
        # self.play(FadeIn(game_circle_2, game_circle_2_text))
        # self.play(AnimationGroup(Create(alice_trans_arrow), Create(alice_trans_text), lag_ratio=0.5))
        # self.play(FadeIn(alice_point_2, alice_point_2_label))

        # self.next_slide()

        # alice_bob_seg = Line(alice_point_2, bob_point, buff=0.1)
        # alice_bob_arrow = Arrow(alice_bob_seg.get_center(), alice_bob_seg.get_center() + DOWN * 2.8, buff=0, max_tip_length_to_length_ratio=0.07)
        # alice_bob_payoff = MyTex(r'$\brmf(\mmx) \bullet \mmy$').next_to(alice_bob_arrow, DOWN, buff=0.2).set_color(BLUE)
        # alice_bob_minmax = MyTex(r'$\displaystyle\max_{\mmx\in \cc{A}} \min_{\mmy\in \cc{B}}$').next_to(alice_bob_payoff, LEFT, buff=0.1).set_color(BLUE).shift(DOWN * 0.1)

        # game_setting = Group(alice_bob_payoff, alice_bob_minmax)

        # self.play(AnimationGroup(Create(alice_bob_seg), Create(alice_bob_arrow), Create(alice_bob_payoff), lag_ratio=0.5))
        
        # self.next_slide()

        # self.play(FadeIn(alice_bob_minmax))

        # self.next_slide()

        # self.play(AnimationGroup(
        #     FadeOut(game_circle_1, game_circle_2, game_polygon, game_circle_1_text, game_circle_2_text, game_polygon_text, 
        #     game_alice, game_bob, alice_point, bob_point, alice_point_2, alice_point_label, bob_point_label, alice_point_2_label, 
        #     alice_bob_arrow, alice_bob_seg, alice_trans_arrow, alice_trans_text),
        #     game_setting.animate.move_to([-1,0,0]).scale(1.3).set_color(WHITE),
        #     lag_ratio = 0.5
        # ))

        # self.next_slide()

        # minimax_theorem_text = MyTex(r'Minimax theorem:').scale(1.3).set_color(BLUE).next_to(game_setting, LEFT, buff=0.2).shift(UP * 0.15)
        # minimax_theorem_eq = MyTex(r'$= \displaystyle\min_{\mmy\in\cc{B}} \displaystyle\max_{\mmx\in\cc{A}}\ \brmf(\mmx)\bullet \mmy = \lambda^*$').scale(1.3).next_to(game_setting, RIGHT, buff=0.15)
        # minimax_theorem_group = Group(game_setting, minimax_theorem_text, minimax_theorem_eq)

        # self.play(Create(minimax_theorem_text))
        # self.play(Create(minimax_theorem_eq))
        # self.wait()
        # self.next_slide()

        # self.play(minimax_theorem_group.animate.scale(1/1.3).next_to(subtitle_game, DOWN, buff=0.5).to_edge(LEFT, buff=1))

        # self.next_slide()

        # nash_equilibrium = MyTex(r'''
        # $\eps$-Nash equilibrium: find $\tilde{\mmx}\in \cc{A}$ and $\tilde{\mmy}\in\cc{B}$ such that
        # \[
        # \begin{aligned}
        #     \min_{\mmy\in \cc{B}}\ \brmf(\tilde{\mmx})\bullet \mmy & \ge \lambda^* - \eps, \\
        #     \max_{\mmx\in \cc{A}}\ \brmf(\mmx)\bullet \tilde{\mmy} & \le \lambda^* + \eps.
        # \end{aligned}
        # \]
        # ''', up=minimax_theorem_group)
        # nash_equilibrium[0][:18].set_color(YELLOW)
        # nash_equilibrium[0][21:25].set_color(RED)
        # nash_equilibrium[0][28:32].set_color(RED)
        # nash_equilibrium[0][48:50].set_color(RED)
        # nash_equilibrium[0][70:72].set_color(RED)

        # self.play(FadeIn(nash_equilibrium))

        # self.next_slide()

        # oracle_intro = MyTex(r'''
        # The {\sc Oracle}: given any $\mmy \in \cc{B}$, provides the best response $\mmx \in \cc{A}$ such that
        # \[
        #     \mmx = \argmax_{\mmx \in \cc{A}}\ \brmf(\mmx) \bullet \mmy
        # \]
        # ''', up=nash_equilibrium)
        # oracle_intro[0][:10].set_color(YELLOW)

        # self.play(FadeIn(oracle_intro))
        # self.next_slide()

        # oracle_width_intro = MyTex(r'''
        # Width $\rho$ of {\sc Oracle}: an upperbound on $\|\brmf(\mmx)\|_\infty$, namely $\|\brmf(\mmx)\|_\infty \le \rho$
        # ''', up=oracle_intro)
        # oracle_width_intro[0][:15].set_color(YELLOW)

        # self.play(FadeIn(oracle_width_intro))
        # self.next_slide()

        # self.play(FadeOut(minimax_theorem_group, oracle_intro, nash_equilibrium, oracle_width_intro))

        # game_thm = Theorem(r'''
        # {\bf\underline{Thm:}} An $\eps$-Nash equilibrium can be found using $O(\rho^2 \log r / \eps^2)$ {\sc Oracle} calls
        # ''')

        # self.play(FadeIn(game_thm))
        # self.next_slide()
        
        # self.play(game_thm.animate.scale(0.5).to_edge(UR, buff=0.5))

        # self.next_slide()

        # game_bob.set_color(WHITE).next_to(subtitle_game, DOWN, buff=0.5).to_edge(LEFT, buff=2)
        # game_alice = Group(game_alice.set_color(WHITE), MyTex(r'({\sc Oracle})').next_to(game_alice, RIGHT, buff=0.1)).next_to(game_bob, RIGHT, buff=3.5)
        # game_payoff = Text("Payoff", color=WHITE).scale(0.6).next_to(game_alice, RIGHT, buff=2)

        # bob_round = [MyTex(r'$\xt{\mmy}{1} = {\mme \over r}$').next_to(game_bob, DOWN, buff=0.5)]
        # alice_round = [MyTex(r'$\xt{\mmx}{1} = \displaystyle\argmax_{\mmx\in\cc{A}} \brmf(\mmx) \bullet \xt{\mmy}{1}$').next_to(game_alice, DOWN, buff=0.5)]
        # alice_round[-1].shift([0, bob_round[-1].get_center()[1] - alice_round[-1].get_center()[1] - 0.1, 0])
        # payoff_round = [MyTex(r'$\brmf(\xt{\mmx}{1}) \bullet \xt{\mmy}{1}$').next_to(game_payoff, DOWN, buff=0.5)]
        # payoff_round[-1].shift([0, bob_round[-1].get_center()[1] - payoff_round[-1].get_center()[1], 0])

        # bob_round.append(MyTex(r'$\xt{\mmy}{2} = {\mmexp\big(-{\eta\over \rho}\brmf(\xt{\mmx}{1})\big) \over \Tr\Big(\mmexp\big(-{\eta\over \rho}\brmf(\xt{\mmx}{1})\big)\Big)}$').next_to(bob_round[-1], DOWN, buff=0.25))
        # alice_round.append(MyTex(r'$\xt{\mmx}{2} = \displaystyle\argmax_{\mmx\in\cc{A}} \brmf(\mmx) \bullet \xt{\mmy}{2}$').next_to(alice_round[-1], DOWN, buff=0.25))
        # alice_round[-1].shift([0, bob_round[-1].get_center()[1] - alice_round[-1].get_center()[1] - 0.1, 0])
        # payoff_round.append(MyTex(r'$\brmf(\xt{\mmx}{2}) \bullet \xt{\mmy}{2}$').next_to(payoff_round[-1], DOWN, buff=0.25))
        # payoff_round[-1].shift([0, bob_round[-1].get_center()[1] - payoff_round[-1].get_center()[1], 0])

        # bob_round.append(MyTex(r'$\xt{\mmy}{3} = {\mmexp\big(-{\eta\over \rho}\sum_{\tau=1}^{2}\brmf(\xt{\mmx}{\tau})\big) \over \Tr\Big(\mmexp\big(-{\eta\over \rho}\sum_{\tau=1}^{2}\brmf(\xt{\mmx}{\tau})\big)\Big)}$').next_to(bob_round[-1], DOWN, buff=0.25))
        # alice_round.append(MyTex(r'$\xt{\mmx}{3} = \displaystyle\argmax_{\mmx\in\cc{A}} \brmf(\mmx) \bullet \xt{\mmy}{3}$').next_to(alice_round[-1], DOWN, buff=0.25))
        # alice_round[-1].shift([0, bob_round[-1].get_center()[1] - alice_round[-1].get_center()[1] - 0.1, 0])
        # payoff_round.append(MyTex(r'$\brmf(\xt{\mmx}{3}) \bullet \xt{\mmy}{3}$').next_to(payoff_round[-1], DOWN, buff=0.25))
        # payoff_round[-1].shift([0, bob_round[-1].get_center()[1] - payoff_round[-1].get_center()[1], 0])

        # vdots = [MyTex(r'$\vdots$') for i in range(3)]
        # vdots[0].next_to(bob_round[-1], DOWN, buff=0.5)
        # vdots[1].next_to(alice_round[-1], DOWN, buff=0.5).shift([0,vdots[0].get_center()[1] - vdots[1].get_center()[1],0])
        # vdots[2].next_to(payoff_round[-1], DOWN, buff=0.5).shift([0,vdots[0].get_center()[1] - vdots[2].get_center()[1],0])

        # bob_round.append(MyTex(r'$\xt{\mmy}{T} = {\mmexp\big(-{\eta\over \rho}\sum_{\tau=1}^{T-1}\brmf(\xt{\mmx}{\tau})\big) \over \Tr\Big(\mmexp\big(-{\eta\over \rho}\sum_{\tau=1}^{T-1}\brmf(\xt{\mmx}{\tau})\big)\Big)}$').next_to(vdots[0], DOWN, buff=0.5))
        # alice_round.append(MyTex(r'$\xt{\mmx}{T} = \displaystyle\argmax_{\mmx\in\cc{A}} \brmf(\mmx) \bullet \xt{\mmy}{T}$').next_to(vdots[1], DOWN, buff=0.5))
        # alice_round[-1].shift([0, bob_round[-1].get_center()[1] - alice_round[-1].get_center()[1] - 0.1, 0])
        # payoff_round.append(MyTex(r'$\brmf(\xt{\mmx}{T}) \bullet \xt{\mmy}{T}$').next_to(vdots[2], DOWN, buff=0.5))
        # payoff_round[-1].shift([0, bob_round[-1].get_center()[1] - payoff_round[-1].get_center()[1], 0])

        # game_avg_line = Line(bob_round[-1].get_left(), payoff_round[-1].get_right() + [0.5,0,0])
        # game_avg_line.shift([0, bob_round[-1].get_bottom()[1] - game_avg_line.get_center()[1] - 0.2, 0])

        # game_avg = []
        # game_avg.append(MyTex(r'$\tilde{\mmy} = {1\over T} \sum_{t=1}^T \xt{\mmy}{t}$').set_color(BLUE).next_to(bob_round[-1], DOWN, buff=0.2))
        # game_avg.append(MyTex(r'$\tilde{\mmx} = {1\over T} \sum_{t=1}^T \xt{\mmx}{t}$').set_color(BLUE).next_to(alice_round[-1], DOWN, buff=0.2))
        # game_avg.append(MyTex(r'${1\over T}\sum_{t=1}^T \brmf(\xt{\mmx}{t}) \bullet \xt{\mmy}{t}$').set_color(BLUE).next_to(payoff_round[-1], DOWN, buff=0.2))
        # for avg in game_avg:
        #     avg.shift([0, game_avg_line.get_bottom()[1] - avg.get_top()[1] - 0.2, 0])

        # game_process_group = Group(game_bob, game_alice, game_payoff, *bob_round, *alice_round, *payoff_round, *vdots, game_avg_line, *game_avg)
        # game_process_group.scale(0.9, about_point=game_process_group.get_top())

        # self.play(FadeIn(game_alice, game_bob, game_payoff))
        # self.next_slide()
        # self.play(FadeIn(bob_round[0]))
        # self.next_slide()
        # self.play(FadeIn(alice_round[0]))
        # self.next_slide()
        # self.play(FadeIn(payoff_round[0]))
        # self.next_slide()
        # self.play(FadeIn(bob_round[1]))
        # self.next_slide()
        # self.play(FadeIn(alice_round[1]))
        # self.next_slide()
        # self.play(FadeIn(payoff_round[1]))
        # self.next_slide()
        # self.play(FadeIn(bob_round[2]))
        # self.wait()
        # self.next_slide()
        # self.play(FadeIn(alice_round[2]))
        # self.next_slide()
        # self.play(FadeIn(payoff_round[2]))
        # self.next_slide()
        # self.play(FadeIn(*vdots, bob_round[-1], alice_round[-1], payoff_round[-1]))
        # self.next_slide()
        # self.play(Create(game_avg_line))
        # self.play(FadeIn(*game_avg))
        # self.wait()
        # self.next_slide()

        # self.play(game_process_group.animate.scale(0.7, about_point=game_process_group.get_top()))
        # self.next_slide()

        # game_claim = Theorem(r'''
        # {\bf\underline{Claim:}}
        # Choose $T = \lceil{4\rho^2 \ln r \over \eps^2}\rceil$ and $\eta = \sqrt{ {\ln r \over T} }$, we have:

        # $\lambda^*\ \overset{(i)}{\le}\ \displaystyle\max_{\mmx\in\cc{A}}\ \brmf(\mmx)\bullet\tilde{\mmy}\ \overset{(ii)}{\le}\ {1\over T}\sum_{t=1}^T \brmf(\xt{\mmx}{t}) \bullet \xt{\mmy}{t} \ \overset{(iii)}{\le}\ \displaystyle\min_{\mmy\in\cc{B}}\ \brmf(\tilde{\mmx})\bullet \mmy + \eps\ \overset{(iv)}{\le}\ \lambda^* + \eps$
        # ''', edge_color=BLUE).scale(0.8).next_to(game_process_group, DOWN, buff=0.3)
        
        # self.play(FadeIn(game_claim))
        # self.next_slide()

        # self.play(FadeOut(game_process_group), game_claim.animate.scale(0.5/0.8).next_to(game_thm, DOWN, buff=0.1).to_edge(RIGHT, buff=0.5))

        # self.wait()
        # self.next_slide()

        # game_proof = []

        # game_proof.append([
        # MyTex(r'''
        # \[ (i)\ \max_{\mmx\in\cc{A}}\ \brmf(\mmx)\bullet \tilde{\mmy}
        #     \ge \min_{\mmy\in\cc{B}} \max_{\mmx\in\cc{A}}\ \brmf(\mmx)\bullet \mmy
        #     = \lambda^* \]
        # '''),
        # MyTex(r'''
        # \[ (i)\ \max_{\mmx\in\cc{A}}\ \brmf(\mmx)\bullet \tilde{\mmy}
        #     \ge \lambda^* \]
        # ''').scale(0.8).next_to(subtitle_game, DOWN, buff=0.5).to_edge(LEFT, buff=1).set_color(BLUE)
        # ])

        # game_proof.append([
        # MyTex(r'''
        # \[ (iv)\ \min_{\mmy\in\cc{B}}\ \brmf(\tilde{\mmx}) \bullet \mmy
        #     \le \max_{\mmx\in\cc{A}} \min_{\mmy\in\cc{B}}\ \brmf(\mmx)\bullet \mmy
        #     = \lambda^* \]
        # '''),
        # MyTex(r'''
        # \[ (iv)\ \min_{\mmy\in\cc{B}}\ \brmf(\tilde{\mmx}) \bullet \mmy + \eps
        #     \le \lambda^* + \eps \]
        # ''').scale(0.8).next_to(game_proof[-1][-1], DOWN, buff=0.25).to_edge(LEFT, buff=1).set_color(BLUE)
        # ])

        # game_proof.append([
        # MyTex(r'''
        # \[ (ii)\ \brmf(\mmx^*)\bullet\xt{\mmy}{t} \le \max_{\mmx \in \cc{A}}\ \brmf(\mmx) \bullet \xt{\mmy}{t} \]
        # '''),
        # MyTex(r'''
        # \[ (ii)\ \brmf(\mmx^*)\bullet\xt{\mmy}{t} \le \brmf(\xt{\mmx}{t}) \bullet \xt{\mmy}{t} \]
        # '''),
        # MyTex(r'''
        # \[ (ii)\ {1\over T} \sum_{t=1}^T \brmf(\mmx^*)\bullet\xt{\mmy}{t} \le {1\over T}\sum_{t=1}^T \brmf(\xt{\mmx}{t}) \bullet \xt{\mmy}{t} \]
        # '''),
        # MyTex(r'''
        # \[ (ii)\ \brmf(\mmx^*)\bullet\tilde{\mmy} \le {1\over T}\sum_{t=1}^T \brmf(\xt{\mmx}{t}) \bullet \xt{\mmy}{t} \]
        # '''),
        # MyTex(r'''
        # \[ (ii)\ \max_{\mmx\in\cc{A}}\ \brmf(\mmx)\bullet\tilde{\mmy} \le {1\over T}\sum_{t=1}^T \brmf(\xt{\mmx}{t}) \bullet \xt{\mmy}{t} \]
        # ''')
        # ])

        # self.play(FadeIn(game_proof[0][0]))
        # self.wait()
        # self.next_slide()
        # self.play(ReplacementTransform(game_proof[0][0], game_proof[0][1]))

        # self.play(FadeIn(game_proof[1][0]))
        # self.wait()
        # self.next_slide()
        # self.play(ReplacementTransform(game_proof[1][0], game_proof[1][1]))

        # self.play(FadeIn(game_proof[2][0]))
        # self.wait()
        # self.next_slide()
        # self.play(ReplacementTransform(game_proof[2][0], game_proof[2][1]))
        # self.wait()
        # self.next_slide()
        # self.play(ReplacementTransform(game_proof[2][1], game_proof[2][2]))
        # self.wait()
        # self.next_slide()
        # self.play(ReplacementTransform(game_proof[2][2], game_proof[2][3]))
        # self.wait()
        # self.next_slide()
        # self.play(ReplacementTransform(game_proof[2][3], game_proof[2][4]))
        # self.wait()
        # self.next_slide()
        # self.play(game_proof[2][4].animate.scale(0.8).next_to(game_proof[1][-1], DOWN, buff=0).to_edge(LEFT, buff=1).set_color(BLUE))
        # self.wait()
        # self.next_slide()

        # game_eigenval_claim = Theorem(r'''
        # {\bf\underline{Claim:}} $\displaystyle {1\over T}\sum_{t=1}^T \brmf(\xt{\mmx}{t}) \bullet \xt{\mmy}{t} \le \lambda_{\min}\Big({1\over T}\sum_{t=1}^T \brmf(\xt{\mmx}{t})\Big) + \eps \le \min_{\mmy\in\cc{B}}\ \brmf(\tilde{\mmx})\bullet \mmy + \eps$
        # ''', edge_color=GREEN).shift(DOWN * 0.5)
        
        # self.play(FadeIn(game_eigenval_claim))
        # self.wait()
        # self.next_slide()

        # self.play(game_eigenval_claim.animate.scale(0.5).next_to(game_claim, DOWN, buff=0.1).to_edge(RIGHT, buff=0.5), FadeOut(game_proof[0][1]), FadeOut(game_proof[1][1]), FadeOut(game_proof[2][4]))

        # self.next_slide()

        # game_eigenval_proof = []
        # game_eigenval_proof.append(
        #     Text('Proof sketch:', color=GREEN).scale(0.5).next_to(subtitle_game, DOWN, buff=1).to_edge(LEFT, buff=1)
        # )
        # game_eigenval_proof.append(
        #     MyTex(r'''\scalebox{0.8}{
        #     $ \xt{\mmw}{1} = \mme,\ \xt{\mmw}{t} = \displaystyle\mmexp\Big(-{\eta\over \rho}\sum_{\tau=1}^{t-1}\brmf(\xt{\mmx}{\tau})\Big) $
        #     } ''', up=game_eigenval_proof[-1], buff=0.25)
        # )
        # game_eigenval_proof.append(
        #     MyTex(r'''\scalebox{0.8}{
        #     Upperbound: $\displaystyle \Tr(\xt{\mmw}{T+1}) \le \Tr(\xt{\mmw}{T})\cdot\exp\Big(- {\eta\over \rho}\brmf(\xt{\mmx}{T})\bullet\xt{\mmy}{T} + {\eta^2\over \rho^2}\big(\brmf(\xt{\mmx}{T})\big)^2\bullet\xt{\mmy}{T}\Big)$
        #     } ''', up=game_eigenval_proof[-1], buff=0.25)
        # )
        # game_eigenval_proof.append(
        #     MyTex(r'''\scalebox{0.8}{
        #     Upperbound: $\displaystyle \Tr(\xt{\mmw}{T+1}) \le r\cdot\exp\Big(-\sum_{t=1}^T {\eta\over \rho} \brmf(\xt{\mmx}{t})\bullet \xt{\mmy}{t} + \sum_{t=1}^T {\eta^2\over \rho^2}\big(\brmf(\xt{\mmx}{t})\big)^2\bullet\xt{\mmy}{t}\Big)$
        #     } ''', up=game_eigenval_proof[-2], buff=0.24)
        # )
        # game_eigenval_proof.append(
        #     MyTex(r'''\scalebox{0.8}{
        #     Lowerbound: $\displaystyle \Tr(\xt{\mmw}{T+1}) \ge \displaystyle\exp\Big(-{\eta\over \rho}\lambda_{\min}\big(\sum_{t=1}^{T}\brmf(\xt{\mmx}{t})\big)\Big)$
        #     } ''', up=game_eigenval_proof[-1], buff=0.25)
        # )

        # self.play(FadeIn(game_eigenval_proof[0]))
        # self.wait()
        # self.next_slide()

        # self.play(FadeIn(game_eigenval_proof[1]))
        # self.wait()
        # self.next_slide()

        # self.play(FadeIn(game_eigenval_proof[2]))
        # self.wait()
        # self.next_slide()

        # self.play(ReplacementTransform(game_eigenval_proof[2], game_eigenval_proof[3]))
        # self.wait()
        # self.next_slide()

        # self.play(FadeIn(game_eigenval_proof[4]))
        # self.wait()
        # self.next_slide()

        # game_eigenval_proof.append([])
        # game_eigenval_proof[-1].append(
        #     MyTex(r'''\scalebox{0.8}{
        #     $\displaystyle r\cdot\exp\Big(-\sum_{t=1}^T {\eta\over \rho} \brmf(\xt{\mmx}{t})\bullet \xt{\mmy}{t} + \sum_{t=1}^T {\eta^2\over \rho^2}\big(\brmf(\xt{\mmx}{t})\big)^2\bullet\xt{\mmy}{t}\Big) \ge \exp\Big(-{\eta\over \rho}\lambda_{\min}\big(\sum_{t=1}^{T}\brmf(\xt{\mmx}{t})\big)\Big) $
        #     } ''', up=game_eigenval_proof[-2], buff=0.25)
        # )
        # game_eigenval_proof[-1].append(
        #     MyTex(r'''\scalebox{0.8}{
        #     $\displaystyle {\rho\ln(r)\over \eta T} -{1\over T} \sum_{t=1}^T \brmf(\xt{\mmx}{t}) \bullet \xt{\mmy}{t} + \eta \rho \ge -{1\over T}\lambda_{\min}\big(\sum_{t=1}^{T}\brmf(\xt{\mmx}{t})\big) = -\lambda_{\min}\big(\brmf(\tilde{\mmx})\big)$
        #     } ''', up=game_eigenval_proof[-2], buff=0.25)
        # )
        # game_eigenval_proof[-1].append(
        #     MyTex(r'''\scalebox{0.8}{
        #     $\displaystyle \eps -{1\over T} \sum_{t=1}^T \brmf(\xt{\mmx}{t}) \bullet \xt{\mmy}{t} \ge -\lambda_{\min}\big(\brmf(\tilde{\mmx})\big)$
        #     } ''', up=game_eigenval_proof[-2], buff=0.25)
        # )

        # self.play(FadeIn(game_eigenval_proof[-1][0]))
        # self.next_slide()
        # self.play(ReplacementTransform(game_eigenval_proof[-1][0], game_eigenval_proof[-1][1]))
        # self.wait()
        # self.next_slide()
        # self.play(ReplacementTransform(game_eigenval_proof[-1][1], game_eigenval_proof[-1][2]))
        # self.wait()
        # self.next_slide()

        # game_eigenval_proof.append(
        #     MyTex(r'''\scalebox{0.9}{
        #     $ \big|{\eta \over \rho}\brmf(\xt{\mmx}{t})\bullet \xt{\mmy}{t}\big| \le 1 \ \Leftarrow \ \|{\eta \over \rho}\brmf(\xt{\mmx}{t})\|_\infty \le 1 \ \Leftarrow \ \|\brmf(\xt{\mmx}{t})\|_\infty \le \rho $
        #     } ''').next_to(game_eigenval_proof[-1][-1], DOWN, buff=0.5).to_edge(LEFT, buff=1).set_color(RED)
        # )

        # self.play(Create(game_eigenval_proof[-1]))
        # self.wait()
        # self.next_slide()

        # self.play(FadeOut(game_thm, game_claim, game_eigenval_claim, game_eigenval_proof[0], game_eigenval_proof[1], game_eigenval_proof[3], game_eigenval_proof[4], game_eigenval_proof[5][2], game_eigenval_proof[-1]))

        # Geometric Optimization ######################################################################################

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

        ## 1. Polytope Distance / Hard-SVM

        ## 2. SEBB

        ## 3. SIB

        ## 4. Soft-SIB


        # # Symmetric Cone Programming ##################################################################################

        # self.play(subtitle_geometry.animate.move_to(outline_pos['subtitle_geometry']),
        #     FadeIn(outline_title, subtitle_eja, subtitle_game, subtitle_scp, subtitle_parallel, subtitle_conclu)
        # )
        # self.next_slide()
        # self.play(subtitle_scp.animate.to_edge(UL, buff=0.5).set_color(WHITE),
        #     FadeOut(outline_title, subtitle_eja, subtitle_game, subtitle_geometry, subtitle_parallel, subtitle_conclu)
        # )
        # self.next_slide()
        
        # # Parallel Computing ##########################################################################################

        # self.play(subtitle_scp.animate.move_to(outline_pos['subtitle_scp']),
        #     FadeIn(outline_title, subtitle_eja, subtitle_game, subtitle_geometry, subtitle_parallel, subtitle_conclu)
        # )
        # self.next_slide()
        # self.play(subtitle_parallel.animate.to_edge(UL, buff=0.5).set_color(WHITE),
        #     FadeOut(outline_title, subtitle_eja, subtitle_game, subtitle_geometry, subtitle_scp, subtitle_conclu)
        # )
        # self.next_slide()

        # inputsize_experiments = NExperiments()
        # self.play(FadeOut(subtitle_parallel))
        # self.play(FadeIn(inputsize_experiments))
        # self.wait()
        # self.next_slide()
        # self.play(FadeOut(inputsize_experiments))

        # dimension_experiments = DExperiments()
        # self.play(FadeIn(dimension_experiments))
        # self.wait()
        # self.next_slide()
        # self.play(FadeIn(subtitle_parallel), FadeOut(dimension_experiments))

        # # Conclusion ##################################################################################################

        # self.play(subtitle_parallel.animate.move_to(outline_pos['subtitle_parallel']),
        #     FadeIn(outline_title, subtitle_eja, subtitle_game, subtitle_geometry, subtitle_scp, subtitle_conclu)
        # )
        # self.next_slide()
        # self.play(subtitle_conclu.animate.to_edge(UL, buff=0.5),
        #     FadeOut(outline_title, subtitle_eja, subtitle_game, subtitle_geometry, subtitle_scp, subtitle_parallel)
        # )
        # self.next_slide()

        # # ENDING #####################################################################################################

        # self.play(FadeOut(subtitle_conclu), FadeIn(Text("Thank you for listening").scale(0.7)))
