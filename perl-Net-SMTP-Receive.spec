%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	SMTP-Receive
Summary:	Net::SMTP::Receive - receive mail via SMTP
Summary(pl):	Net::SMTP::Receive - odbieraj±cy pocztê protoko³em SMTP
Name:		perl-%{pdir}-%{pnam}
Version:	0.2
Release:	3
License:	Freely distributable
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::SMTP::Receive handles receiving email via SMTP.  It is built as
a base class that must be subclassed to provide methods for actually
delivering a message.  Many aspects of Net::SMTP::Receive's behavior
can be modified by overriding methods in the subclass.

%description -l pl
Modu³ Net::SMTP::Receive obs³uguje odbieranie poczty po SMTP. Jest
zbudowany jako klasa bazowa, z której nale¿y dziedziczyæ, aby
udostêpniæ metody do w³a¶ciwego dostarczania wiadomo¶ci. Wiele
aspektów zachowania Net::SMTP::Receive mo¿e byæ modyfikowanych poprzez
pokrywanie metod w podklasie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp example_daemon.pl $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/Net/SMTP/*.pm
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/*
