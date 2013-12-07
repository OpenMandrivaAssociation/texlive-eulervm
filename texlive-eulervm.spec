# revision 15878
# category Package
# catalog-ctan /fonts/eulervm
# catalog-date 2006-12-09 23:51:48 +0100
# catalog-license lppl
# catalog-version 4.0
Name:		texlive-eulervm
Version:	4.0
Release:	5
Summary:	Euler virtual math fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/eulervm
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eulervm.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eulervm.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eulervm.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The well-known Euler fonts are suitable for typsetting
mathematics in conjunction with a variety of text fonts which
do not provide mathematical character sets of their own. Euler-
VM is a set of virtual mathematics fonts based on Euler and CM.
This approach has several advantages over immediately using the
real Euler fonts: Most noticeably, less TeX resources are
consumed, the quality of various math symbols is improved and a
usable \hslash symbol can be provided. The virtual fonts are
accompanied by a LaTeX package which makes them easy to use,
particularly in conjunction with Type1 PostScript text fonts.
They are compatible with amsmath. A package option allows the
fonts to be loaded at 95% of their nominal size, thus blending
better with certain text fonts, e.g., Minion.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/tfm/public/eulervm/zeuex10.tfm
%{_texmfdistdir}/fonts/tfm/public/eulervm/zeurb10.tfm
%{_texmfdistdir}/fonts/tfm/public/eulervm/zeurb5.tfm
%{_texmfdistdir}/fonts/tfm/public/eulervm/zeurb7.tfm
%{_texmfdistdir}/fonts/tfm/public/eulervm/zeurm10.tfm
%{_texmfdistdir}/fonts/tfm/public/eulervm/zeurm5.tfm
%{_texmfdistdir}/fonts/tfm/public/eulervm/zeurm7.tfm
%{_texmfdistdir}/fonts/tfm/public/eulervm/zeusb10.tfm
%{_texmfdistdir}/fonts/tfm/public/eulervm/zeusb5.tfm
%{_texmfdistdir}/fonts/tfm/public/eulervm/zeusb7.tfm
%{_texmfdistdir}/fonts/tfm/public/eulervm/zeusm10.tfm
%{_texmfdistdir}/fonts/tfm/public/eulervm/zeusm5.tfm
%{_texmfdistdir}/fonts/tfm/public/eulervm/zeusm7.tfm
%{_texmfdistdir}/fonts/vf/public/eulervm/zeuex10.vf
%{_texmfdistdir}/fonts/vf/public/eulervm/zeurb10.vf
%{_texmfdistdir}/fonts/vf/public/eulervm/zeurb5.vf
%{_texmfdistdir}/fonts/vf/public/eulervm/zeurb7.vf
%{_texmfdistdir}/fonts/vf/public/eulervm/zeurm10.vf
%{_texmfdistdir}/fonts/vf/public/eulervm/zeurm5.vf
%{_texmfdistdir}/fonts/vf/public/eulervm/zeurm7.vf
%{_texmfdistdir}/fonts/vf/public/eulervm/zeusb10.vf
%{_texmfdistdir}/fonts/vf/public/eulervm/zeusb5.vf
%{_texmfdistdir}/fonts/vf/public/eulervm/zeusb7.vf
%{_texmfdistdir}/fonts/vf/public/eulervm/zeusm10.vf
%{_texmfdistdir}/fonts/vf/public/eulervm/zeusm5.vf
%{_texmfdistdir}/fonts/vf/public/eulervm/zeusm7.vf
%{_texmfdistdir}/tex/latex/eulervm/eulervm.sty
%{_texmfdistdir}/tex/latex/eulervm/uzeuex.fd
%{_texmfdistdir}/tex/latex/eulervm/uzeur.fd
%{_texmfdistdir}/tex/latex/eulervm/uzeus.fd
%doc %{_texmfdistdir}/doc/latex/eulervm/README.eulervm
%doc %{_texmfdistdir}/doc/latex/eulervm/eulervm.pdf
%doc %{_texmfdistdir}/doc/latex/eulervm/manifest.txt
#- source
%doc %{_texmfdistdir}/source/latex/eulervm/eulervm.dtx
%doc %{_texmfdistdir}/source/latex/eulervm/eulervm.ins
%doc %{_texmfdistdir}/source/latex/eulervm/fontinst/Makefile
%doc %{_texmfdistdir}/source/latex/eulervm/fontinst/amsrel10.mtx
%doc %{_texmfdistdir}/source/latex/eulervm/fontinst/amsrel5.mtx
%doc %{_texmfdistdir}/source/latex/eulervm/fontinst/amsrel7.mtx
%doc %{_texmfdistdir}/source/latex/eulervm/fontinst/axis10.mtx
%doc %{_texmfdistdir}/source/latex/eulervm/fontinst/axis5.mtx
%doc %{_texmfdistdir}/source/latex/eulervm/fontinst/axis7.mtx
%doc %{_texmfdistdir}/source/latex/eulervm/fontinst/eubar10.mtx
%doc %{_texmfdistdir}/source/latex/eulervm/fontinst/eubar5.mtx
%doc %{_texmfdistdir}/source/latex/eulervm/fontinst/eubar7.mtx
%doc %{_texmfdistdir}/source/latex/eulervm/fontinst/euml.etx
%doc %{_texmfdistdir}/source/latex/eulervm/fontinst/eums.etx
%doc %{_texmfdistdir}/source/latex/eulervm/fontinst/eumx.etx
%doc %{_texmfdistdir}/source/latex/eulervm/fontinst/fontevm.tex
%doc %{_texmfdistdir}/source/latex/eulervm/fontinst/unsetams.mtx
%doc %{_texmfdistdir}/source/latex/eulervm/fontinst/unseteus.mtx
%doc %{_texmfdistdir}/source/latex/eulervm/fontinst/unsetex.mtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 4.0-2
+ Revision: 751662
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 4.0-1
+ Revision: 718385
- texlive-eulervm
- texlive-eulervm
- texlive-eulervm
- texlive-eulervm

