%define		ver   1.0
%define		sdate 20060126
Summary:	A program to build tty dialog boxes
Summary(de):	Ein Programm zum Erstellen von tty-Dialogfeldern
Summary(fr):	Programme pour construire des boîtes de dialogue en mode texte
Summary(pl):	Dialog tworzy okienkowy interfejs u¿ytkownika na terminalu tekstowym
Summary(tr):	tty diyalog kutularý oluþturan bir program
Name:		dialog
Version:	%{ver}.%{sdate}
Release:	0.9
Epoch:		1
License:	LGPL v2.1
Group:		Applications/Terminal
Source0:	ftp://invisible-island.net/dialog/%{name}-%{ver}-%{sdate}.tgz
# Source0-md5:	48dc347ac316fb40bf2ab36d955d0cc7
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	932081790cd8aa857822bd2b0eafa5bb
Patch0:		%{name}-examples.patch
URL:		http://invisible-island.net/dialog/dialog.html
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
Benutzeroberfläche in einem TTY ermöglicht (nur Textmodus). Sie können
dialog mit einem Shell-Script aufrufen, um dem Benutzer auf
benutzerfreundliche Weise Fragen zu stellen oder eine Auswahl
anzubieten. Unter /usr/src/examples/dialog-%{version} finden Sie
einige Beispiele.

%description -l fr
dialog est un utilitaire permettant de construire des interfaces
utilisateur en mode texte. On peut appeler dialog à partir d'un script
shell pour poser des questions à l'utilisateur ou lui proposer des
choix de façon conviviale. Voir /usr/src/examples/dialog-%{version}
pour quelques exemples.

%description -l pl
Dialog jest narzêdziem umo¿liwiaj±cym stworzenie przyjaznego
interfejsu u¿ytkownika na terminalu pracuj±cym w trybie tekstowym. Do
programu do³±czone s± przyk³adowe skrypty, u³atwiaj±ce rozpoczêcie
pracy.

%description -l tr
Dialog, metin ekran için kullanýcý arayüzleri oluþturmayý saðlayan bir
araçtýr. Kullanýcýya seçenekleri göstermek veya sorular sormak için,
dialog programýný bir kabuk programcýðý içinden çaðýrabilirsiniz.
Örnekler için /usr/src/examples/dialog-%{version} dizinine bakýnýz.

%package devel
Summary:	Libraries and headers files for dialog
Summary(pl):	Biblioteki i pliki nagó³wkowe dla dialog
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}

%description devel
Libraries and header files for dialog.

%description devel -l pl
Biblioteki i pliki nag³ówkowe dla dialog.

%package static
Summary:	Static dialog library
Summary(pl):	Statyczna biblioteka dialog
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}

%description static
Static dialog library.

%description static -l pl
Statyczna biblioteka dialog.

%prep
%setup -q -n %{name}-%{ver}-%{sdate}
#patch0 -p1 - example scripts need similar fixes 

%build
%configure \
	--with-libtool \
	--with-ncursesw \
	--enable-widec \
	--enable-nls

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_examplesdir}/%{name}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -a samples/* dialog.pl $RPM_BUILD_ROOT%{_examplesdir}/%{name}

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dialog
%attr(755,root,root) %{_libdir}/lib*.so.*
%{_mandir}/man1/*
%lang(hu) %{_mandir}/hu/man1/*
%lang(pl) %{_mandir}/pl/man1/*

%files devel
%defattr(644,root,root,755)
%doc README CHANGES
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_mandir}/man3/*
%attr(- ,root,root) %{_examplesdir}/dialog

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
