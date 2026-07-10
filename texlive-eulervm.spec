%global tl_name eulervm
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.0
Release:	%{tl_revision}.1
Summary:	Euler virtual math fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/eulervm
License:	lppl1.1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/eulervm.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/eulervm.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/eulervm.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The well-known Euler fonts are suitable for typesetting mathematics in
conjunction with a variety of text fonts which do not provide
mathematical character sets of their own. Euler-VM is a set of virtual
mathematics fonts based on Euler and CM. This approach has several
advantages over immediately using the real Euler fonts: Most noticeably,
less TeX resources are consumed, the quality of various math symbols is
improved and a usable \hslash symbol can be provided. The virtual fonts
are accompanied by a LaTeX package which makes them easy to use,
particularly in conjunction with Type1 PostScript text fonts. They are
compatible with amsmath. A package option allows the fonts to be loaded
at 95% of their nominal size, thus blending better with certain text
fonts, e.g., Minion.

