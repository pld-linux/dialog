Summary:	A program to build tty dialog boxes
Summary(de):	Ein Programm zum Erstellen von tty-Dialogfeldern
Summary(fr):	Programme pour construire des bo�tes de dialogue en mode texte
Summary(pl):	Dialog tworzy okienkowy interfejs u�ytkownika na terminalu tekstowym
Summary(tr):	tty diyalog kutular� olu�turan bir program
Name:		dialog
Version:	0.69
Release:	5
Epoch:		1
License:	GPL
Group:		Applications/Terminal
Group(de):	Applikationen/Terminal
Group(pl):	Aplikacje/Terminal
Source0:	ftp://AdvancedResearch.org/pub/vstemen/%{name}-%{version}.tar.gz
Source1:	dialog-non-english-man-pages.tar.bz2
Patch0:		%{name}-shared.patch
Patch1:		%{name}-manpath.patch
Patch2:		%{name}-awk.patch
Patch3:		%{name}-examples.patch
Patch4:		%{name}-opt.patch
URL:		http://www.AdvancedResearch.org/dialog
BuildRequires:	autoconf
BuildRequires:	gpm-devel
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dialog is a utility that allows you to build user interfaces in a TTY
(text mode only). You can call dialog from within a shell script to
ask the user questions or present with choices in a more user friendly
manner.

%description -l de
Dialog ist ein Dienstprogramm, das das Erstellen einer
Benutzeroberfl�che in einem TTY erm�glicht (nur Textmodus). Sie k�nnen
dialog mit einem Shell-Script aufrufen, um dem Benutzer auf
benutzerfreundliche Weise Fragen zu stellen oder eine Auswahl
anzubieten. Unter /usr/src/examples/dialog-%{version} finden Sie
einige Beispiele.

%description -l fr
dialog est un utilitaire permettant de construire des interfaces
utilisateur en mode texte. On peut appeler dialog � partir d'un script
shell pour poser des questions � l'utilisateur ou lui proposer des
choix de fa�on conviviale. Voir /usr/src/examples/dialog-%{version}
pour quelques exemples.

%description -l pl
Dialog jest narz�dziem umo�liwiaj�cym stworzenie przyjaznego
interfejsu u�ytkownika na terminalu pracuj�cym w trybie tekstowym. Do
programu do��czone s� przyk�adowe skrypty, u�atwiaj�ce rozpocz�cie
pracy.

%description -l tr
Dialog, metin ekran i�in kullan�c� aray�zleri olu�turmay� sa�layan bir
ara�t�r. Kullan�c�ya se�enekleri g�stermek veya sorular sormak i�in,
dialog program�n� bir kabuk programc��� i�inden �a��rabilirsiniz.
�rnekler i�in /usr/src/examples/dialog-%{version} dizinine bak�n�z.

%package devel
Summary:	Libraries and headers files for dialog
Summary(pl):	Biblioteki i pliki nag�wkowe dla dialog
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	����������/����������
Group(uk):	��������/��̦�����
Requires:	%{name} = %{version}

%description devel
Libraries and header files for dialog.

%description devel -l pl
Biblioteki i pliki nag��wkowe dla dialog.

%package static
Summary:	Static dialog library
Summary(pl):	Statyczna biblioteka dialog
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	����������/����������
Group(uk):	��������/��̦�����
Requires:	%{name}-devel = %{version}

%description static
Static dialog library.

%description static -l pl
Statyczna biblioteka dialog.

%prep
%setup  -q
%patch0 -p1 
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
autoconf
%configure

%{__make} depend shared all

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_examplesdir}/%{name}}

%{__make} install \
    prefix=$RPM_BUILD_ROOT%{_prefix} \
    mandir=$RPM_BUILD_ROOT%{_mandir}

cp -a samples/* dialog.pl $RPM_BUILD_ROOT%{_examplesdir}/%{name}

bzip2 -dc %{SOURCE1} | tar -xf - -C $RPM_BUILD_ROOT%{_mandir}

gzip -9nf dialog.lsm README CMDLINE

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dialog
%attr(755,root,root) %{_libdir}/lib*.so.*
%{_mandir}/man1/*
%lang(hu) %{_mandir}/hu/man1/*
%lang(pl) %{_mandir}/pl/man1/*

%files devel
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*
%{_mandir}/man3/*
%attr(- ,root,root) %{_examplesdir}/dialog

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
