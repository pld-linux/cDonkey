Summary:	Open source core client for eDonkey
Name:		cDonkey
Version:	0.5.0
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://suche.org/%{name}-%{version}.tar.bz2
URL:		http://cdonkey.suche.org/
BuildRequires:	db-devel >= 4.1
BuildRequires:	openssl-devel
BuildRequires:	zlib-devel 
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cDonkey is an open source core client for eDonkey without a GUI. It
works together with eMule and ed2k_gui. It uses Berkley DB-4.1 for
fast List management. The eMule Packet data and source2source exchange
was implemented. It currently only works with Linux.

%prep
%setup -q

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
%doc TODO
