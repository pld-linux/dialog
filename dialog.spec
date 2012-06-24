Summary:	A program to build tty dialog boxes
Summary(de):	Ein Programm zum Erstellen von tty-Dialogfeldern
Summary(fr):	Programme pour construire des bo�tes de dialogue en mode texte
Summary(pl):	Dialog tworzy okienkowy interfejs u�ytkownika na terminalu tekstowym
Summary(tr):	tty diyalog kutular� olu�turan bir program
Name:		dialog
Version:	0.69
Release:	1
License:	GPL
Group:		Utilities/Terminal
Group(pl):	Narz�dzia/Terminal
Source0:	ftp://iride.unipv.it/pub/linux/dialog/%{name}-%{version}.tar.gz
Patch0:		dialog-shared.patch
Patch1:		dialog-manpath.patch
Patch2:		dialog-awk.patch
Patch3:		dialog-examples.patch
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
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Libraries and headers files for dialog.

%description devel -l pl
Biblioteki i pliki nag�wkowe dla dialog.

%package	static
Summary:	Static dialog library
Summary(pl):	Statyczna biblioteka dialog
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
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

%build
autoconf && %configure

%{__make} depend shared all

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/{bin,share/man/man1,src/examples/dialog}

%{__make} \
    prefix=$RPM_BUILD_ROOT%{_prefix} \
    mandir=$RPM_BUILD_ROOT%{_mandir} \
    install

cp -a samples/* dialog.pl $RPM_BUILD_ROOT%{_prefix}/src/examples/dialog

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc dialog.lsm README CMDLINE

%attr(755,root,root) %{_bindir}/dialog
%attr(755,root,root) %{_libdir}/lib*.so.*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)

%attr(- ,root,root) %{_prefix}/src/examples/dialog
%attr(755,root,root) %{_libdir}/lib*.so

%{_includedir}/*
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)

%{_libdir}/lib*.a
