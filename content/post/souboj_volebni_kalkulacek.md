---
title: "Souboj volebních kalkulaček"
date: 2017-10-05T04:50:00+02:00
draft: false
image: "/img/cs.jpg"
categories: ["Volební kalkulačka"]
tags: ["volební kalkulačka", "volby"]
---
<style> td {border-bottom: 1px solid #dddddd; border-right: 1px solid #dddddd;} </style>
Volební kalkulačky jsou dnes pro lidi jedním z podstatných předvolebních zdrojů. Před volbami je v Česku, v závislosti na typu voleb, použije něco <b>mezi 10 a 25 % voličů, ale letos to velice pravděpodobně bude ještě více</b>. Ve Skandinávii nebo Nizozemí je to už přes 50 % voličů.

Dvěma třetinám uživatelů volební kalkulačka pomůže s výběrem strany a <b>20 % lidí dokonce přesvědčí, aby volili l někoho jiného</b>, než před tím chtěli. Data vycházejí je z <a href="https://ecpr.eu/Events/PaperDetails.aspx?PaperID=37081&EventID=96">výzkumu Düsseldorfské univerzity</a>, který byl prezentován na konferenci ECPR (hlavní politologická konference v Evropě) minulý měsíc.

Zde je čas zdůraznit, že se volebními kalkulačkami zabývám prakticky i teoreticky (viz např. <a href="https://ecpr.eu/Events/PaperDetails.aspx?PaperID=37097&EventID=96">tento příspěvek z konference ECPR</a>) už <b>přes deset let</b>, jsem také hlavní autor největší české <a href="https://volebnikalkulacka.cz">Volební kalkulačky</a> ("s velkým V"). A poslední měsíc a půl s ní trávím téměř každý den, od programování až po výběr otázek a jsem si tak vědom mnoha problémů, které má. (A také spolu s kolegy připravujeme podstatné vylepšení pro prezidentské volby, na což zrovna <a href="https://www.hithit.com/cs/project/4067/volebni-kalkulacka-on-steroids">sháníme podporu pomocí crowdfundingu na Hithitu</a>.)

<h3>Kalkulačka vs. test</h3>
Proto když Aktuálně.cz zveřejnilo svůj <a href="https://zpravy.aktualne.cz/domaci/volebni-test-odpovezte-na-otazky-dozvite-se-komu-dat-hlas/r~034d2064a38511e79142002590604f2e/">Volební test</a>, profesionální povinnost logicky velela jej hned prostudovat. Zapůsobil na mě ale jako studená sprcha, což jsem asi trochu neuváženě hned ventiloval na Twitteru, kde pak došlo k <a href="https://twitter.com/skopmichal/status/914775919281283072">poměrně ostré výměně názorů mezi šéfredaktorem Aktuálně.cz p. Tomáškem a mnou</a>. Snad to moc nedezinterpretuji, když to shrnu: Já tvrdím, že Aktuálně.cz převzalo skoro polovinu otázek z Volební kalkulačky bez uvedení zdroje, p. Tomášek píše, že naše otázky při přípravě neviděli a že je tedy osočuji zcela neprávem. '<i>Neuváženě</i>' píši proto, že to vlastně není důležitá otázka.

My nakonec i <a href="https://github.com/KohoVolit/vaa2012-2">zveřejňujeme</a> celou Volební kalkulačku (kód i obsah) pod otevřenými licencemi, aby pomohla co největšímu počtu lidí. A jestli lidem pomůže kalkulačka pod jménem <i>Volební test Aktuálně.cz</i> nebo pod názvem <i>Volební kalkulačka</i>, je vcelku jedno. <b>Hlavně, když to pomůže</b>.

Tak se tedy raději podívejme, zda <i>Volební test Aktuálně.cz</i> slouží uživatelům dobře. A zde je z mého pohledu <b>závažný problém</b>.

<i>Volební test Aktuálně.cz</i> vypadá na první pohled velice obdobně jako <i>Volební kalkulačka</i> – uživatel může (zde i musí) odpovědět na otázky ‚Ano‘, ‚Ne‘ nebo ‚Nevím‘. Shoda mezi uživatelem a stranou je zobrazena pomocí počtu shodných odpovědí. Proč ne. Nicméně <b>ďábel je skryt v detailu</b>.

Nejlépe to ukázat na příkladu níže.

<h3>Co poradit Adéle</h3>
<i>Adéla bydlí v Aši a neví, zda má volit stranu A se sympatickou političkou v čele, stranu B vedenou inteligentní profesorkou s fialově obarvenými vlasy, nebo stranu C vedenou charismatickým leaderem. Tak zkusí volební kalkulačky: Volební kalkulačku a Volební test Aktuálně.cz. Obě kalkulačky obsahují zcela náhodou stejné otázky, tak si postoje stran i Adély můžeme napsat do jedné tabulky:

<table>    <thead>        <tr>            <th style="font-weight:bold">                Otázka            </th>            <th style="font-weight:bold">                Strana A            </th>            <th style="font-weight:bold">                Strana B            </th>            <th style="font-weight:bold">                Strana C            </th>            <th style="font-weight:bold">                Adéla            </th>        </tr>    </thead>    <tbody>        <tr>            <td>                ČR by měla vystoupit z EU.            </td>            <td>                <b>Ne</b>            </td>            <td>                Nemáme jednotný postoj, ½ chce vystoupit, ½ ne            </td>            <td>                <b>Ano</b>            </td>            <td>                <b>Ne</b>            </td>        </tr>        <tr>            <td>                Těšínsko by se mělo přípojit k Polsku.            </td>            <td>                Ne            </td>            <td>                Ne            </td>            <td>                Nevíme            </td>            <td>                Nevím - Je mi to srdečně jedno, bydlím v Aši, kde je Těšínsko?            </td>            <tr>                <td>                    Fialová barva je nejlepší barva.                </td>                <td>                    Nemáme jednotný postoj                </td>                <td>                    Ano                </td>                <td>                    Nemáme jednotný postoj                </td>                <td>                    Nerozumím otázce, v čem nejlepší? Přeskakuji                </td>            </tr>        </tr>    </tbody></table>

<b>Volební kalkulačka</b> ji doporučí <b>stranu A</b>. <b>Volební test Aktuálně.cz</b> ji doporučí <b>stranu C.</b>

Volební kalkulačka bere, že pro Adélu byla důležitá jenom jedna otázka (EU), tak zbylé 2 otázky ve formulaci rady pro Adélu vůbec neuvažuje. Adéla chce zůstat v EU a zde se shodne se stranou A a naopak zcela neshodne se stranou C.

Adéla dostane tento výsledek:

<table style="min-width:50%">    <tbody>        <tr>            <td>                1. Strana A            </td>            <td>                ***** 100 %            </td>        </tr>        <tr>            <td>                2. Strana B            </td>            <td>                *** 50 %            </td>        </tr>        <tr>            <td>                3. Strana B            </td>            <td>                * 0 %            </td>        </tr>    </tbody></table>

Ovšem Volební test Aktuálně Adéle doporučí stranu C, protože se dle něj Adéla se stranou C shoduje ve 2 otázkách (Těšínsko, fialová), zatímco se stranou A a B pak v jedné:

<table style="min-width:50%">    <tbody>        <tr>            <td>                1. Strana C            </td>            <td>                shoda ve 2 otázkách            </td>        </tr>        <tr>            <td>                2.-3. Strana B            </td>            <td>                shoda v 1 otázce            </td>        </tr>        <tr>            <td>                2.-3. strana A            </td>            <td>                shoda v 1 otázce            </td>        </tr>    </tbody></table>

Nemůžu si pomoci, ale Volební test Aktuálně.cz Adéle <b>poradil špatně</b>.</i>

Za shodnou odpověď <i>Volební test Aktuálně.cz</i> totiž považuje i to, že uživatel odpoví ‚Nevím‘ a strana také neodpověděla ani ‚Ano‘, ani ‚Ne‘ (zde ještě není jasné, jak se přesně Aktuálně stran ptalo, zda tam byla možnost ‚Nevíme‘ nebo něco jiného). A to je velký problém.

<h3>Není 'Nevím' jako 'Nevím'</h3>
‚Nevím‘, ani Ano ani Ne, totiž <b>může znamenat plno věcí</b>: ‚Nerozumím otázce‘, ‚Otázka mě nezajímá‘, ‚Otázka pro mě není jednoznačná – někdy Ano, někdy Ne‘, atd. Stejně tak strana, pokud neodpoví ‚Ano‘ ani ‚Ne‘, může mít více důvodů: ‚Nemáme na danou věc jednotný názor, část strany je pro, část proti‘, ‚Není to pro nás vůbec důležité‘, atd.

Příklad s Adélou je jistě extrémní. Nastává ten problém i u reálných uživatelů? Co víme o uživatelích Volební kalkulačky, tak ti dávají <b>neutrální odpověď nebo přeskakují dál u nějakých 15 % – 20 % otázek + dalších 5 – 10 % je neutrálních odpovědí u stran</b>. Tedy není to tak špatné jako u Adély, ale pořád jde o velice podstatný problém.

Volební kalkulačky neslouží jenom k tomu, aby lidem pomohli s výběrem strany před volbami. Jistě jsou např. <b>edukativní</b> v tom, že ukazují, co vše politici řeší. Nebo z výzkumů víme, že <b>podporují volební účast</b>. Tyto další funkce jistě plní i <i>Volební test Aktuálně.cz</i>.

Nicméně celkem vzhledem k tomu problému s počítáním neutrálních odpovědí musím říci, že za sebe bych doporučil se <i>Volebnímu testu Aktuálně.cz</i> vyhnout. Ale třeba ten výpočet ještě upraví, nic složitého to zase není.

<i>Napsáno pro <a href="http://hlidacipes.org/souboj%E2%80%8B-%E2%80%8Bvolebnich%E2%80%8B-%E2%80%8Bkalkulacek%E2%80%8B-%E2%80%8B-%E2%80%8Bjak-cist-rady/">Hlídacího psa</a></i>.
