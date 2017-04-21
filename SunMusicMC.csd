; BROTHER SUN (2010) for realtime Csound5 - by Arthur B. Hunkins
;  Requires 1 or more MIDI devices with a total of 8 or 9 pots/sliders
;  Multiple Controller version - Csound 5.10 or greater

<CsoundSynthesizer>
<CsOptions>

-odac -+rtaudio=alsa -+rtmidi=alsa -Ma -m0d --expression-opt -b128 -B2048 -+raw_controller_mode=1

</CsOptions>
<CsInstruments>
	
sr	=	32000
ksmps	=	100
nchnls  =       2

        instr 1

ichan   chnget  "Chan"
ictrl   chnget  "Cont"
ipan    chnget  "Pan"
ipctrl  chnget  "PCont"
imult   chnget  "Mult"
kmod1	ctrl7   (ichan = 0? 1: ichan), (ichan = 0? 7: ictrl), 0, 7
iport	=	(imult == 0? .1: .3)
kmod1   port    kmod1, iport
kmod2	ctrl7   (ichan = 0? 2: ichan), (ichan = 0? 7: ictrl + 1), 0, 10
kmod2   port    kmod2, iport
kmod3	ctrl7   (ichan = 0? 3: ichan), (ichan = 0? 7: ictrl + 2), 0, 13
kmod3   port    kmod3, iport
kmod4	ctrl7   (ichan = 0? 4: ichan), (ichan = 0? 7: ictrl + 3), 0, 16
kmod4   port    kmod4, iport
kmod5	ctrl7   (ichan = 0? 5: ichan), (ichan = 0? 7: ictrl + 4), 0, 19
kmod5   port    kmod5, iport
kmod6	ctrl7   (ichan = 0? 6: ichan), (ichan = 0? 7: ictrl + 5), 0, 22
kmod6   port    kmod6, iport
kfreq	ctrl7   (ichan = 0? 7: ichan), (ichan = 0? 7: ictrl + 6), 50, 55
kfreq   port    kfreq, 1.5, 50
krand   rspline -.1, .1, .5, .8
krand2  rspline -.1, .1, .5, .8
krand3  rspline -.1, .1, .5, .8
krand4  rspline -.1, .1, .5, .8
krand5  rspline -.1, .1, .5, .8
amod1	lfo	kfreq * kmod1, kfreq * 2
amod2	lfo	kfreq * kmod2, (kfreq * 3) + krand
amod3	lfo	kfreq * kmod3, (kfreq * 5) + krand2
amod4	lfo	kfreq * kmod4, (kfreq * 7) + krand3
amod5	lfo	kfreq * kmod5, (kfreq * 9) + krand4
amod6	lfo	kfreq * kmod6, (kfreq * 11) + krand5
kamp2	ctrl7   (ichan = 0? 8: ichan), (ichan = 0? 7: ictrl + 7), 0, 1
kamp    table   kamp2 * 512, 1
kamp	=	(kamp2 == 0? 0: kamp * 25000)
kamp    port    kamp, iport
kramp   jspline -.15 * kamp, 1, 3.5
aout	oscil	kamp + kramp, amod1 + amod2 + amod3 + amod4 + amod5 + amod6, 2
        if ipan = 0 goto skip
kpan    ctrl7   (ichan = 0? 9: ichan), (ichan = 0? 7: ipctrl), 0, 1
kpan    port    kpan, .5
a1,a2,a3,a4  pan    aout, kpan, 1, 3, 1
	outs	a1, a2
        goto fin
skip:   outs    aout, aout        
fin:    endin

</CsInstruments>
<CsScore>

f1 0 512 16 1 511 2.2 1000
f2 0 16384 10 1
f3 0 8193 7 0 8193 1
i1 0 3600

</CsScore>
</CsoundSynthesizer>
