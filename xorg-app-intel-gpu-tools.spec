Summary:	Tools for Intel DRM driver
Summary(pl.UTF-8):	Narzędzia do sterownika Intel DRM
Name:		xorg-app-intel-gpu-tools
Version:	1.8
Release:	2
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/archive/individual/app/intel-gpu-tools-%{version}.tar.bz2
# Source0-md5:	49d2c3c65204d889189c4d8c14c598b3
URL:		http://intellinuxgraphics.org/
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.10
BuildRequires:	bison
BuildRequires:	cairo-devel >= 1.12.0
BuildRequires:	glib2-devel >= 2.0
%if %(locale -a | grep -q '^en_US\.UTF-8$'; echo $?)
BuildRequires:	glibc-localedb-all
%endif
BuildRequires:	gtk-doc >= 1.14
BuildRequires:	libdrm-devel >= 2.4.52
BuildRequires:	libtool >= 2:2.2
BuildRequires:	pkgconfig
BuildRequires:	python3-devel >= 3.0
BuildRequires:	sed >= 4.0
BuildRequires:	swig-python >= 2.0.0
BuildRequires:	udev-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXrandr-devel >= 1.3
BuildRequires:	xorg-lib-libXv-devel
BuildRequires:	xorg-lib-libpciaccess-devel >= 0.10
BuildRequires:	xorg-proto-dri2proto-devel >= 2.6
BuildRequires:	xorg-util-util-macros >= 1.16
Requires:	cairo >= 1.12.0
Requires:	libdrm >= 2.4.52
Requires:	xorg-lib-libXrandr >= 1.3
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

%{__sed} -i -e '1s,#!/usr/bin/env python3,#!/usr/bin/python3,' tools/quick_dump/{quick_dump,reg_access}.py

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules

# python needs UTF-8 locale to read non-ascii debugger/system_routine/*.g4a files
LC_ALL=en_US.UTF-8 \
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/I*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/chipset.py
%attr(755,root,root) %{_bindir}/eudb
%attr(755,root,root) %{_bindir}/gem_userptr_benchmark
%attr(755,root,root) %{_bindir}/intel-gen4asm
%attr(755,root,root) %{_bindir}/intel-gen4disasm
%attr(755,root,root) %{_bindir}/intel-gpu-overlay
%attr(755,root,root) %{_bindir}/intel_*
%attr(755,root,root) %{_bindir}/quick_dump.py
%attr(755,root,root) %{_bindir}/reg_access.py
%attr(755,root,root) %{_libdir}/I915ChipsetPython.so
%{_pkgconfigdir}/intel-gen4asm.pc
%{_mandir}/man1/intel_*.1*
