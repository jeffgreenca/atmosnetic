# concept


```
data source(s) -> aggregated data source
                       |
                       v
                    controller
	(per-instrument subprocess, responsible for "playing" instrument)

  instrument a
  instrument b   ===>  DSP (Mastering Effects, Reverb etc.) ===> DarkIce live audio streamer -->  ShoutCast/IceCast
  instrument c
  ...

Where: 
  ===> are JACK audio routing
  instrument: any process that results in audio to jack input (could be csound render-and-play, MIDI synth, text-to-speech, etc.)
```
