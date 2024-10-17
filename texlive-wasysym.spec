Name:		texlive-wasysym
Version:	54080
Release:	2
Summary:	LaTeX support file to use the WASY2 fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/wasysym
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/wasysym.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/wasysym.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/wasysym.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The WASY2 (Waldi Symbol) font by Roland Waldi provides many
glyphs like male and female symbols and astronomical symbols,
as well as the complete lasy font set and other odds and ends.
The wasysym package implements an easy to use interface for
these symbols.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/wasysym
%doc %{_texmfdistdir}/doc/latex/wasysym
#- source
%doc %{_texmfdistdir}/source/latex/wasysym

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
