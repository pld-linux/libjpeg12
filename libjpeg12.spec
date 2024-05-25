Summary:	Library for handling different JPEG files - 12-bit version
Summary(pl.UTF-8):	Biblioteka do manipulacji plikami w formacie JPEG - wersja 12-bitowa
Name:		libjpeg12
Version:	9f
Release:	1
License:	distributable
Group:		Libraries
Source0:	http://www.ijg.org/files/jpegsrc.v%{version}.tar.gz
# Source0-md5:	9ca58d68febb0fa9c1c087045b9a5483
Patch0:		libjpeg-maxmem-sysconf.patch
Patch1:		libjpeg-12bit.patch
URL:		http://www.ijg.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The libjpeg package contains a library of functions for manipulating
JPEG images. This package is built with 12 bits per sample.

%description -l pl.UTF-8
Ten pakiet zawiera bibliotekę funkcji do manipulacji plikami JPEG. Ta
wersja została zbudowana z 12-bitową rozdzielczością próbkowania.

%package devel
Summary:	Headers for developing programs using libjpeg12
Summary(pl.UTF-8):	Pliki nagłówkowe libjpeg12
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package includes the header files necessary for developing
programs which will manipulate JPEG files using the libjpeg
library. This version is built with 12 bits per sample.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki potrzebne do programowania z wykorzystaniem
biblioteki libjpeg. Ta wersja została zbudowana z 12-bitową
rozdzielczością próbkowania.

%package static
Summary:	Static library for developing programs using libjpeg12
Summary(pl.UTF-8):	Biblioteka statyczna libjpeg12
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static library for developing programs using libjpeg12.

%description static -l pl.UTF-8
Statyczna biblioteka libjpeg12.

%prep
%setup -q -n jpeg-%{version}
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--includedir=%{_includedir}/libjpeg12 \
	--disable-silent-rules \
	--enable-shared \
	--enable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install jversion.h $RPM_BUILD_ROOT%{_includedir}/libjpeg12

# remove HAVE_STD{DEF,LIB}_H
# (not necessary but may generate warnings confusing autoconf)
sed -i -e 's#.*HAVE_STD..._H.*##g' $RPM_BUILD_ROOT%{_includedir}/libjpeg12/jconfig.h

# tools packaged in generic libjpeg
%{__rm} -r $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README change.log
%attr(755,root,root) %{_libdir}/libjpeg12.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libjpeg12.so.9

%files devel
%defattr(644,root,root,755)
%doc libjpeg.txt structure.txt
%attr(755,root,root) %{_libdir}/libjpeg12.so
%{_libdir}/libjpeg12.la
%{_includedir}/libjpeg12
%{_pkgconfigdir}/libjpeg12.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libjpeg12.a
