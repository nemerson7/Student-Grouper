
def name_to_last_first(name):
    first = name.split()[0]
    last = name.split()[1]
    return last + ", " + first

def name_to_first_last(name):
    first = name.split(", ")[1]
    last = name.split(", ")[0]
    return first + " " + last

texdoc = r"""\documentclass[11pt, oneside]{article}   	% use "amsart" instead of "article" for AMSLaTeX format
\usepackage{geometry}                		% See geometry.pdf to learn the layout options. There are lots.
\geometry{letterpaper}                   		% ... or a4paper or a5paper or ... 
%\geometry{landscape}                		% Activate for rotated page geometry
%\usepackage[parfill]{parskip}    		% Activate to begin paragraphs with an empty line rather than an indent
\usepackage{graphicx}				% Use pdf, png, jpg, or eps§ with pdflatex; use eps in DVI mode
								% TeX will automatically convert eps --> pdf in pdflatex		
\usepackage{amssymb}

%SetFonts

%SetFonts


\title{Groups for Assignment NUMBER_HERE}


\date{}							% Activate to display a given date or no date

\addtolength{\oddsidemargin}{-.675in}
\addtolength{\evensidemargin}{-.675in}
\begin{document}
\maketitle
%\section{}
%\subsection{}
\begin{flushleft}
\begin{small}
\begin{tabular}{||c c c c c||} 
 \hline
Group Number & Member 1 & Member 2 & Member 3 & Member 4\\ [0.5ex] 
 \hline\hline
 TABLE_HERE
\end{tabular}
\end{small}
\end{flushleft}

\end{document}  
"""
