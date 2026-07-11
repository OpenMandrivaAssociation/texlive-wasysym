%global tl_name wasysym
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.4
Release:	%{tl_revision}.1
Summary:	LaTeX support for the wasy fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/wasysym
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/wasysym.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/wasysym.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/wasysym.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The wasy (Waldi Symbol) font by Roland Waldi provides many glyphs like
male and female symbols and astronomical symbols, as well as the
complete lasy font set and other odds and ends. This package implements
an easy to use interface for these symbols.

