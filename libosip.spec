%define name	libosip
%define version	0.9.7
%define release	%mkrel 5

%define fakename osip

%define major 0
%define libname %mklibname %{fakename} %major
%define libnamedev %mklibname %{fakename} %major -d

Name:		%name
Summary:	Implementation of SIP - rfc2543. 
Version: 	%version
Release: 	%release
License: 	LGPL
Group:		System/Libraries
Source0:	%{name}-%{version}.tar.bz2
URL: 		http://osip.atosc.org/
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	docbook-utils docbook-dtd41-sgml

%description
This is the oSIP library (for Open SIP). It has been
designed to provide the Internet Community a simple
way to support the Session Initiation Protocol.
SIP is described in the RFC2543 which is available at
http://www.ietf.org/rfc/rfc2543.txt.

%package -n %libname
Summary:        Header file required to build programs using liboSIP
Group:          System/Libraries

%description -n %libname
This is the oSIP library (for Open SIP). It has been
designed to provide the Internet Community a simple
way to support the Session Initiation Protocol.
SIP is described in the RFC2543 which is available at
http://www.ietf.org/rfc/rfc2543.txt.

%package -n %libnamedev
Summary:	Header file required to build programs using liboSIP
Group:		System/Libraries 
Provides: libosip-devel
Requires: %libname = %version

%description -n %libnamedev
oSIP development libraries (for Open SIP). Needed to build applications
such as Linphone

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q
perl -p -i -e 's/docbook-to-man/docbook2man/g' doc/Makefile.in

%build
%configure
%make

%install
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%files -n %libname
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%_libdir/*.so.*
%_mandir/man1/*

%files -n %libnamedev
%defattr(-, root, root)
%_libdir/*.so
%_includedir/osip
%_libdir/*.a
%_libdir/*.la

