%define debug_package %{nil}

Summary:	A Java wrapper around theora, using JNA
Name:		theora-java
Version:	20071009
Release:	0.0.6
License:	LGPLv3
Group:		Development/Java
URL:		http://fmj.sourceforge.net/
#Source0:	%{name}-%{version}-1153.tar.gz
Source0:	%{name}.tar.bz2
Patch:		%{name}-build.xml.diff
BuildRequires:	ant
BuildRequires:	java-rpmbuild >= 1.5
BuildRequires:	jorbis
BuildRequires:	update-alternatives
BuildRequires:	xml-commons-apis
Requires:	java >= 1.5
Requires:	jorbis
Requires:	libogg
Requires:	libtheora
Requires:	libvorbis

%description
theora-java is a Java wrapper around theora, using JNA.

%package javadoc
Summary:	Javadoc for theora-java
Group:		Development/Java

%description javadoc
Javadoc for theora-java.

%prep
%setup -q -n %{name}
%patch0

%__rm lib/jogg*.jar
%__rm lib/jorbis*.jar

%build
%ant dist

%install
# jar
%__install -dm 755 %{buildroot}%{_javadir}/fmj
%__install -pm 644 build/jars/%{name}.jar \
	%{buildroot}%{_javadir}/fmj/%{name}-%{version}.jar
pushd %{buildroot}%{_javadir}/fmj
	for jar in *-%{version}*; do
		ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`
	done
popd
%__install -pm 644 build/jars/jheora-patch.jar \
	%{buildroot}%{_javadir}/fmj

# javadoc
%__install -dm 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr build/doc/* \
	%{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name} 

%files
%defattr(-,root,root)
%doc *.txt README
%dir %{_javadir}/fmj
%{_javadir}/fmj/*.jar

%files javadoc
%defattr(0644,root,root,0755)
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}


%changelog
* Sat Nov 22 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 20071009-0.0.5mdv2009.1
+ Revision: 305922
- no longer noarch, as it uses arch specific libraries

* Fri Nov 21 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 20071009-0.0.4mdv2009.1
+ Revision: 305606
- fix requires on theora for mdv releases older than 200910

* Fri Nov 07 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 20071009-0.0.3mdv2009.1
+ Revision: 300810
- fix requires on libtheora
- new license policy
- spec file clean

* Mon Sep 22 2008 Alexander Kurtakov <akurtakov@mandriva.org> 20071009-0.0.2mdv2009.0
+ Revision: 287017
- bump release
- fix requires

* Mon Sep 22 2008 Alexander Kurtakov <akurtakov@mandriva.org> 20071009-0.0.1mdv2009.0
+ Revision: 286736
- import theora-java


