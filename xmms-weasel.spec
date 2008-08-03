%define name xmms-weasel
%define version 0.0.1
%define release %mkrel 8

Summary: Hide XMMS window automatically
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: Sound
Url: http://xmms-weasel.sourceforge.net
BuildRequires: xmms-devel
Requires: xmms
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: chrpath


%description
XMMS Weasel is a general plugin for XMMS. XMMS Weasel automatically
slides out XMMS from the screen as soon as the mouse pointer is
leaving the XMMS window.  If the mouse pointer hits the edge of the
screen where XMMS was hidden, XMMS slides back in.  XMMS Weasel is
only active if XMMS is docked at the top of the screen.

%prep
%setup -q

%build
%define __libtoolize true
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -f %buildroot%_libdir/xmms/General/libweasel.la
chrpath -d %buildroot%_libdir/xmms/General/libweasel.so
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc NEWS README ChangeLog
%_libdir/xmms/General/libweasel.so

