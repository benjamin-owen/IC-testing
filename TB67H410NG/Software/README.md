# Software

## pwm_modulate.py

This program uses SCPI commands to interact with a function generator and modulate a PWM signal

Program can be run with 0, 1, or 5 arguments

### Arguments:

pwm_modulate.py (addr) (freq) (pwm_low) (pwm_high) (delay)

- addr: Address of function generator "USB::XXXX"
- freq: Frequency of PWM signal (Hz)
- pwm_low: Minimum duty cycle during modulation (%)
- pwm_high: Maximum duty cycle during modulation (%)
- delay: Time for one modulation cycle (low-high-low) (seconds)
