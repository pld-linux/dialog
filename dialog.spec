Summary: 	A program to build tty dialog boxes
Summary(de): 	Ein Programm zum Erstellen von tty-Dialogfeldern  
Summary(fr): 	Programme pour construire des boîtes de dialogue en mode texte
Summary(pl):	Dialog tworzy okienkowy interfejs u¿ytkownika na terminalu tekstowym.
Summary(tr): 	tty diyalog kutularý oluþturan bir program
Name: 		dialog
Version: 	0.6
Release: 	15
Copyright: 	GPL
Group: 		Utilities/Terminal
Group(pl):	Narzêdzia/Terminal
Source: 	ftp://ftp.redhat.com/pub/misc/%{name}-%{version}.tar.gz
Patch: 	        dialog-ncurses.patch
Patch1: 	dialog-opt.patch
Patch2: 	dialog-loop.patch
BuildPrereq:	ncurses-devel
Buildroot:	/tmp/buildroot-%{name}-%{version}

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

%prep
%setup  -q
%patch0 -p1 
%patch1 -p1 
%patch2 -p1 

%build
( cd src; make depend )

make 

%install
rm -rf $RPM_BUILD_ROOT 
install -d $RPM_BUILD_ROOT/usr/{bin,man/man1,src/examples/%{name}-%{version}}

install -s src/dialog $RPM_BUILD_ROOT/usr/bin
install man/dialog.man $RPM_BUILD_ROOT/usr/man/man1/dialog.1
cp -a samples $RPM_BUILD_ROOT/usr/src/examples/%{name}-%{version}

gzip -9nf $RPM_BUILD_ROOT/usr/man/man*/* \
	dialog.lsm README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {dialog.lsm,README}.gz
%doc /usr/src/examples/%{name}-%{version}
%attr(755,root,root) /usr/bin/dialog
/usr/man/man1/dialog.1*


%changelog
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
