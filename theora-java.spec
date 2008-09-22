Name:			theora-java
Summary:		A Java wrapper around theora, using JNA
Version:		20071009
Release:		%mkrel 0.0.1
License:		LGPL
Group:			Development/Java
URL:			http://fmj.sourceforge.net/
#Source0:		%{name}-%{version}-1153.tar.gz
Source0:		%{name}.tar.bz2
Patch:			%{name}-build.xml.diff
BuildRoot:		%{_tmppath}/%{name}-%{version}-build
BuildArch:		noarch
BuildRequires:	ant
BuildRequires:	java-rpmbuild >= 1.5
BuildRequires:	jorbis
BuildRequires:	update-alternatives
BuildRequires:	xml-commons-apis
Requires:		java >= 1.5
Requires:		jorbis
Requires:		libogg
Requires:		libtheora
Requires:		libvorbis

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
%__cp -pr build/doc/* \
	%{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name} 

%clean
[ -d %{buildroot} -a "%{buildroot}" != "" ] && %__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc *.txt LICENSE README
%dir %{_javadir}/fmj
%{_javadir}/fmj/*.jar

%files javadoc
%defattr(0644,root,root,0755)
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}
