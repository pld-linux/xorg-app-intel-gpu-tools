Summary:	Tools for Intel DRM driver
Summary(pl.UTF-8):	Narzędzia do sterownika Intel DRM
Name:		xorg-app-intel-gpu-tools
Version:	1.2
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/archive/individual/app/intel-gpu-tools-%{version}.tar.bz2
# Source0-md5:	08c860aa4d067c4ee10c5a672092f2d8
URL:		http://intellinuxgraphics.org/
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.10
BuildRequires:	cairo-devel
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	libdrm-devel >= 2.4.31
BuildRequires:	libtool >= 2:2.2
BuildRequires:	udev-devel
BuildRequires:	xorg-lib-libpciaccess-devel >= 0.10
BuildRequires:	xorg-util-util-macros >= 1.16
Requires:	libdrm >= 2.4.31
Requires:	xorg-lib-libpciaccess >= 0.10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a collection of tools for development and testing of the Intel
DRM driver.

%description -l pl.UTF-8
Ten pakiet zawiera zestaw narzędzi do rozwijania i testowania
sterownika Intel DRM.

%prep
%setup -q -n intel-gpu-tools-%{version}

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/forcewaked
%attr(755,root,root) %{_bindir}/intel_*
%attr(755,root,root) %{_bindir}/sprite_on
%{_mandir}/man1/intel_*.1*
