Summary:	Open source core client for eDonkey
Summary(pl):	Otwarty rdzeñ klienta sieci eDonkey
Name:		cDonkey
Version:	0.8.9
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://suche.org/%{name}-%{version}.tar.bz2
# Source0-md5:	a1a5eb43697b8f098f80709f017ab84c
URL:		http://cdonkey.suche.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	db-devel >= 4.1
BuildRequires:	libtool
BuildRequires:	openssl-devel >= 0.9.7c
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Provides:	eDonkey-core

%description
cDonkey is an open source core client for eDonkey without a GUI. It
works together with eMule and ed2k_gui. It uses Berkeley DB-4.1 for
fast List management. The eMule Packet data and source2source exchange
was implemented. It currently only works with Linux.

%description -l pl
cDonkey jest otwartym rdzeniem klienta sieci eDonkey bez interfejsu
graficznego. Wspó³gra z eMule oraz ed2k_gui. U¿ywa bazy Berkeley w
wersji 4.1 do szybkiego zarz±dzania listami. Dzia³a tylko na Linuksie.

%prep
%setup -q -n %{name}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -D cDonkey $RPM_BUILD_ROOT%{_bindir}/cDonkey

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%doc TODO FAQ-EN README
