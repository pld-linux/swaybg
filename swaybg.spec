Summary:	Wallpaper tool for Wayland compositors
Name:		swaybg
Version:	1.2.1
Release:	1
License:	MIT
Group:		Applications
Source0:	https://github.com/swaywm/swaybg/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	a0228fadd684cd778d46b70756088178
URL:		https://github.com/swaywm/swaybg
BuildRequires:	cairo-devel
BuildRequires:	gdk-pixbuf2-devel
BuildRequires:	meson >= 0.59.0
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	scdoc
BuildRequires:	wayland-devel >= 1.14.91
BuildRequires:	wayland-protocols >= 1.26
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
swaybg is a wallpaper utility for Wayland compositors. It is
compatible with any Wayland compositor which implements the following
Wayland protocols:

- wlr-layer-shell
- xdg-output
- xdg-shell

%prep
%setup -q

%build
%meson build
%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/swaybg
%{_mandir}/man1/swaybg.1*
