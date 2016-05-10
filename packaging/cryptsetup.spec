Name: cryptsetup
Summary: A utility for setting up encrypted disks
Version: 1.6.7
Release: 1
License: GPL-2.0
Group: Base/Device Management
URL: https://gitlab.com/cryptsetup/cryptsetup
Source0: cryptsetup-%{version}.tar.xz
Source1: cryptsetup.manifest

BuildRequires: linux-kernel-headers
BuildRequires: device-mapper-devel
BuildRequires: libgpg-error-devel
BuildRequires: libgcrypt-devel
BuildRequires: libuuid-devel
BuildRequires: util-linux
BuildRequires: popt-devel
BuildRequires: automake
BuildRequires: gettext

Requires: libgpg-error
Requires: libdevmapper
Requires: libgcrypt

%description
The cryptsetup package contains a utility for setting up
disk encryption using dm-crypt kernel module.

%package devel
Summary: Headers and libraries for using encrypted file systems
Group: Development/Libraries
License: LGPL-2.1
Requires: %{name} = %{version}-%{release}
Requires: libgcrypt-devel > 1.1.42
Requires: device-mapper-devel
Requires: libuuid-devel
Requires: pkgconfig

%description devel
The cryptsetup-devel package contains libraries and header files
used for writing code that makes use of disk encryption.

%package locale
Summary: Cryptsetup locale package
Group: Base/Device Management
License: GPL-2.0
Requires: %{name} = %{version}-%{release}

%description locale
locale package for cryptsetup

%package doc
Summary: Cryptsetup doc package
Group: Base/Device Management
License: GPL-2.0
Requires: %{name} = %{version}-%{release}

%description doc
doc package for cryptsetup

%prep
%setup -q

%build
./autogen.sh --prefix=%{_prefix} -localedir=%{_prefix}/share/locale

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install
cp -a %{SOURCE1} %{buildroot}%{_datadir}/binary_package_name.manifest

%clean

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%manifest %{_datadir}/binary_package_name.manifest
%{_prefix}/lib/libcryptsetup.so
%{_prefix}/lib/libcryptsetup.so.4
%{_prefix}/lib/libcryptsetup.so.4.7.0
%{_prefix}/sbin/cryptsetup
%{_prefix}/sbin/veritysetup

%files devel
%{_prefix}/include/libcryptsetup.h
%{_prefix}/lib/libcryptsetup.so
%{_prefix}/lib/pkgconfig/libcryptsetup.pc

%files locale
%{_prefix}/share/locale/cs/LC_MESSAGES/cryptsetup.mo
%{_prefix}/share/locale/de/LC_MESSAGES/cryptsetup.mo
%{_prefix}/share/locale/fi/LC_MESSAGES/cryptsetup.mo
%{_prefix}/share/locale/fr/LC_MESSAGES/cryptsetup.mo
%{_prefix}/share/locale/id/LC_MESSAGES/cryptsetup.mo
%{_prefix}/share/locale/it/LC_MESSAGES/cryptsetup.mo
%{_prefix}/share/locale/nl/LC_MESSAGES/cryptsetup.mo
%{_prefix}/share/locale/pl/LC_MESSAGES/cryptsetup.mo
%{_prefix}/share/locale/sv/LC_MESSAGES/cryptsetup.mo
%{_prefix}/share/locale/uk/LC_MESSAGES/cryptsetup.mo
%{_prefix}/share/locale/vi/LC_MESSAGES/cryptsetup.mo
%{_prefix}/share/locale/es/LC_MESSAGES/cryptsetup.mo

%files doc
%{_prefix}/share/man/man8/cryptsetup.8.gz
%{_prefix}/share/man/man8/veritysetup.8.gz
