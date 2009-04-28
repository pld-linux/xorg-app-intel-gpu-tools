Summary:	Tools for Intel DRM driver
Name:		xorg-app-intel-gpu-tools
Version:	1.0
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/archive/individual/app/intel-gpu-tools-%{version}.tar.gz
# Source0-md5:	fa363e7b4f0e6290b92a151d433238e9
URL:		http://intellinuxgraphics.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libdrm-devel
BuildRequires:	xorg-lib-libpciaccess-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a collection of tools for development and testing of the Intel
DRM driver.

%prep
%setup -q -n intel-gpu-tools-%{version}

%build
%{__aclocal} -I m4
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
%attr(755,root,root) %{_bindir}/*
