# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/wasysym
# catalog-date 2006-12-16 22:36:42 +0100
# catalog-license lppl
# catalog-version 2.0
Name:		texlive-wasysym
Version:	2.0
Release:	1
Summary:	LaTeX support file to use the WASY2 fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/wasysym
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/wasysym.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/wasysym.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/wasysym.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The WASY2 (Waldi Symbol) font by Roland Waldi provides many
glyphs like male and female symbols and astronomical symbols,
as well as the complete lasy font set and other odds and ends.
The wasysym package implements an easy to use interface for
these symbols.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/wasysym/uwasy.fd
%{_texmfdistdir}/tex/latex/wasysym/uwasyvar.fd
%{_texmfdistdir}/tex/latex/wasysym/wasysym.sty
%doc %{_texmfdistdir}/doc/latex/wasysym/wasysym.pdf
%doc %{_texmfdistdir}/doc/latex/wasysym/wasysym.upl
%doc %{_texmfdistdir}/doc/latex/wasysym/wasysym.xml
#- source
%doc %{_texmfdistdir}/source/latex/wasysym/wasysym.dtx
%doc %{_texmfdistdir}/source/latex/wasysym/wasysym.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
