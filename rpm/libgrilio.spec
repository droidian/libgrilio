Name: libgrilio

Version: 1.0.41
Release: 0
Summary: RIL I/O library
License: BSD
URL: https://github.com/sailfishos/libgrilio
Source: %{name}-%{version}.tar.bz2

%define libglibutil_version 1.0.10

BuildRequires: pkgconfig
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(libglibutil) >= %{libglibutil_version}
Requires: libglibutil >= %{libglibutil_version}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
Provides glib-based RIL I/O library

%package devel
Summary: Development library for %{name}
Requires: %{name} = %{version}

%description devel
This package contains the development library for %{name}.

%prep
%setup -q

%build
make %{_smp_mflags} LIBDIR=%{_libdir} KEEP_SYMBOLS=1 release pkgconfig

%install
rm -rf %{buildroot}
make LIBDIR=%{_libdir} DESTDIR=%{buildroot} install-dev

%check
make -C test test

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license LICENSE
%{_libdir}/%{name}.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/*.pc
%{_libdir}/%{name}.so
%{_includedir}/grilio/*.h
