Summary: 	A program to build tty dialog boxes
Summary(de): 	Ein Programm zum Erstellen von tty-Dialogfeldern  
Summary(fr): 	Programme pour construire des boîtes de dialogue en mode texte
Summary(pl):	Dialog tworzy okienkowy interfejs u¿ytkownika na terminalu tekstowym.
Summary(tr): 	tty diyalog kutularý oluþturan bir program
Name: 		dialog
Version: 	0.69
Release: 	1
Copyright: 	GPL
Group: 		Utilities/Terminal
Group(pl):	Narzêdzia/Terminal
Source: 	ftp://iride.unipv.it/pub/linux/dialog/%{name}-%{version}.tar.gz
Patch0:		dialog-shared.patch
BuildPrereq:	ncurses-devel
BuildPrereq:	gpm-devel
Requires:	%{name}-libs = %{version}
Buildroot:	/tmp/%{name}-%{version}-root

%description
Dialog is a utility that allows you to build user interfaces in
a TTY (text mode only).  You can call dialog from within a shell
script to ask the user questions or present with choices in a more
user friendly manner.  See /usr/doc/dialog-*/samples for some
examples.

%description -l de
Dialog ist ein Dienstprogramm, das das Erstellen einer Benutzeroberfläche
in einem TTY ermöglicht (nur Textmodus). Sie können dialog mit einem
Shell-Script aufrufen, um dem Benutzer auf benutzerfreundliche Weise
Fragen zu stellen oder eine Auswahl anzubieten. Unter
/usr/src/examples/dialog-%{version} finden Sie einige Beispiele.

%description -l fr
dialog est un utilitaire permettant de construire des interfaces
utilisateur en mode texte. On peut appeler dialog à partir d'un
script shell pour poser des questions à l'utilisateur ou lui
proposer des choix de façon conviviale. 
Voir /usr/src/examples/dialog-%{version} pour quelques exemples.

%description -l pl
Dialog jest narzêdziem umo¿liwiaj±cym stworzenie przyjaznego interfejsu
u¿ytkownika na terminalu pracuj±cym w trybie tekstowym. Do programu
do³±czone s± przyk³adowe skrypty, u³atwiaj±ce rozpoczêcie pracy.

%description -l tr
Dialog, metin ekran için kullanýcý arayüzleri oluþturmayý saðlayan bir
araçtýr. Kullanýcýya seçenekleri göstermek veya sorular sormak için, dialog
programýný bir kabuk programcýðý içinden çaðýrabilirsiniz. Örnekler için
/usr/src/examples/dialog-%{version} dizinine bakýnýz.

%package libs
Summary:	Dialog library
Summary(pl):	Biblioteka dialog
Group:		Libraries
Group(pl):	Biblioteki

%description libs
Dialog library.

%description libs -l pl
Biblioteka dialog pozwala na stworzenie przyjaznego interfejsu
u¿ytkownika na terminalu pracuj±cym w trybie tekstowym.

%package devel
Summary:	Libraries and headers files for dialog
Summary(pl):	Biblioteki i pliki nagó³wkowe dla dialog
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-libs = %{version}

%description devel
Libraries and headers files for dialog.

%description devel -l pl
Biblioteki i pliki nagó³wkowe dla dialog.

%package static
Summary:	Static dialog library
Summary(pl):	Statyczna biblioteka dialog
Group:		Development/Libraries
Group(pl):      Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static dialog library.

%description static -l pl
Statyczna biblioteka dialog.

%prep
%setup  -q
%patch0 -p1 

%build
autoconf

CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target} \
	--prefix=/usr

make depend shared all

%install
rm -rf $RPM_BUILD_ROOT 
install -d $RPM_BUILD_ROOT/usr/{bin,man/man1,src/examples/%{name}-%{version}}

make prefix=$RPM_BUILD_ROOT/usr install

cp -a samples/* dialog.pl $RPM_BUILD_ROOT/usr/src/examples/%{name}-%{version}

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man*/* \
	dialog.lsm README CMDLINE

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {dialog.lsm,README,CMDLINE}.gz
%attr(755,root,root) %{_bindir}/dialog
%{_mandir}/man1/*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc /usr/src/examples/%{name}-%{version}/checklist
%doc /usr/src/examples/%{name}-%{version}/gauge-sh
%doc /usr/src/examples/%{name}-%{version}/gauge.c
%doc /usr/src/examples/%{name}-%{version}/infobox
%doc /usr/src/examples/%{name}-%{version}/inputbox
%doc /usr/src/examples/%{name}-%{version}/menubox
%doc /usr/src/examples/%{name}-%{version}/msgbox
%doc /usr/src/examples/%{name}-%{version}/radiolist
%doc /usr/src/examples/%{name}-%{version}/textbox
%doc /usr/src/examples/%{name}-%{version}/yesno
%doc /usr/src/examples/%{name}-%{version}/README
%doc /usr/src/examples/%{name}-%{version}/Makefile
%doc %attr(755,root,root) /usr/src/examples/%{name}-%{version}/gauge

%attr(755,root,root) %{_libdir}/lib*.so
/usr/include/*
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%changelog
* Wed Apr 28 1999 Artur Frysiak <wiget@pld.org.pl>
  [0.69-1]
- upgrade to 0.69
- changed source URL
- added libs, devel and static subpackage
- fixed coping samples

* Thu Apr 22 1999 Artur Frysiak <wiget@pld.org.pl>
  [0.6-15]
- compiled on rpm 3
- gzipped docs
- samples moved to /usr/src/examples

* Sun Oct 18 1998 Marcin Korzonek <mkorz@shadow.eu.org>
  [0.6-13]
- added pl translation,
- allow building from non root account,
- defined files permission,
- removed INSTALL and COPYING from docs,
- rewritten %install section.

* Thu May 7 1998 Michael Maher <mike@redhat.com> 
- Added Sean Reifschneider <jafo@tummy.com> patches for 
  infinite loop problems.

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 15 1998 Erik Troan <ewt@redhat.com>
- built against new ncurses

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
