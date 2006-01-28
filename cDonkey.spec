Summary:	Open source core client for eDonkey
Summary(pl):	Otwarty rdze� klienta sieci eDonkey
Name:		cDonkey
Version:	0.9.0
Release:	3
License:	GPL
Group:		Applications/Communications
Source0:	http://suche.org/%{name}-%{version}.tar.bz2
# Source0-md5:	04c7b16e2aeb18a246e9892ba6fe7b7a
Patch0:		%{name}-in_addr.patch
Patch1:		%{name}-types.patch
Patch2:		%{name}-nolibs.patch
URL:		http://cdonkey.suche.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	db-devel >= 4.1
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	zlib-devel
Provides:	eDonkey-core
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cDonkey is an open source core client for eDonkey without a GUI. It
works together with eMule and ed2k_gui. It uses Berkeley DB-4.1 for
fast List management. The eMule Packet data and source2source exchange
was implemented. It currently only works with Linux.

%description -l pl
cDonkey jest otwartym rdzeniem klienta sieci eDonkey bez interfejsu
graficznego. Wsp�gra z eMule oraz ed2k_gui. U�ywa bazy Berkeley w
wersji 4.1 do szybkiego zarz�dzania listami. Dzia�a tylko na Linuksie.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
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
%doc TODO FAQ-EN README
%attr(755,root,root) %{_bindir}/*
