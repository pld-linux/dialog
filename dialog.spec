Summary: 	A program to build tty dialog boxes
Name: 		dialog
Version: 	0.6
Release: 	13
Copyright: 	GPL
Group: 		Utilities/Terminal
Group(pl):	Narz�dzia/Terminal
Source: 	ftp://ftp.redhat.com/pub/misc/%{name}-%{version}.tar.gz
Patch: 	        %{name}-%{version}-ncurses.patch
Patch1: 	%{name}-%{version}-opt.patch
Patch2: 	%{name}-%{version}-loop.patch
Buildroot:	/tmp/buildroot-%{name}-%{version}
Summary(de): 	Ein Programm zum Erstellen von tty-Dialogfeldern  
Summary(fr): 	Programme pour construire des bo�tes de dialogue en mode texte
Summary(pl):	Dialog tworzy okienkowy interfejs u�ytkownika na terminalu tekstowym.
Summary(tr): 	tty diyalog kutular� olu�turan bir program

%description
Dialog is a utility that allows you to build user interfaces in
a TTY (text mode only).  You can call dialog from within a shell
script to ask the user questions or present with choices in a more
user friendly manner.  See /usr/doc/dialog-*/samples for some
examples.

%description -l de
Dialog ist ein Dienstprogramm, das das Erstellen einer Benutzeroberfl�che
in einem TTY erm�glicht (nur Textmodus). Sie k�nnen dialog mit einem
Shell-Script aufrufen, um dem Benutzer auf benutzerfreundliche Weise
Fragen zu stellen oder eine Auswahl anzubieten. Unter
/usr/doc/dialog-*/samples finden Sie einige Beispiele.

%description -l fr
dialog est un utilitaire permettant de construire des interfaces
utilisateur en mode texte. On peut appeler dialog � partir d'un
script shell pour poser des questions � l'utilisateur ou lui
proposer des choix de fa�on conviviale. Voir /usr/doc/dialog-*/samples
pour quelques exemples.

%description -l pl
Dialog jest narz�dziem umo�liwiaj�cym stworzenie przyjaznego interfejsu
u�ytkownika na terminalu pracuj�cym w trybie tekstowym. Do programu
do��czone s� przyk�adowe skrypty, u�atwiaj�ce rozpocz�cie pracy.

%description -l tr
Dialog, metin ekran i�in kullan�c� aray�zleri olu�turmay� sa�layan bir
ara�t�r. Kullan�c�ya se�enekleri g�stermek veya sorular sormak i�in, dialog
program�n� bir kabuk programc��� i�inden �a��rabilirsiniz. �rnekler i�in
/usr/doc/dialog-*/samples dizinine bak�n�z.

%prep
%setup -q
%patch -p1 
%patch1 -p1 
%patch2 -p1 
cd src
make depend

%build
make 

%install
rm -rf $RPM_BUILD_ROOT 
install -d $RPM_BUILD_ROOT/usr/{bin,man/man1}

install -s src/dialog $RPM_BUILD_ROOT/usr/bin
install man/dialog.man $RPM_BUILD_ROOT/usr/man/man1/dialog.1

gzip -9nf $RPM_BUILD_ROOT/usr/man/man*/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc dialog.lsm README samples
%attr(755, root, root) /usr/bin/dialog
%attr(644, root,  man) /usr/man/man1/dialog.1


%changelog
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
