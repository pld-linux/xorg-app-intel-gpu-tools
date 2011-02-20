Summary:	Tools for Intel DRM driver
Summary(pl.UTF-8):	Narzędzia do sterownika Intel DRM
Name:		xorg-app-intel-gpu-tools
Version:	1.0.2
Release:	1
License:	MIT
Group:		X11/Applications
#Source0:	http://xorg.freedesktop.org/archive/individual/app/intel-gpu-tools-%{version}.tar.gz
Source0:	http://cgit.freedesktop.org/xorg/app/intel-gpu-tools/snapshot/intel-gpu-tools-41570d9bf583d35687bab88ac88620af41404836.tar.bz2
# Source0-md5:	9dad8596ecfb9c2d39dda70963bba236
URL:		http://intellinuxgraphics.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libdrm-devel >= 2.4.6
BuildRequires:	xorg-lib-libpciaccess-devel >= 0.10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a collection of tools for development and testing of the Intel
DRM driver.

%description -l pl.UTF-8
Ten pakiet zawiera zestaw narzędzi do rozwijania i testowania
sterownika Intel DRM.

%prep
%setup -qc
mv intel-gpu-tools-*/* .

%build
%{__aclocal} -I m4
%{__libtoolize}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
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
%attr(755,root,root) %{_bindir}/intel_*
%{_mandir}/man1/intel_*.1*
