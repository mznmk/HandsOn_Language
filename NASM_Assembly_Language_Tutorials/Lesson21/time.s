%include	'functions.s'

SECTION		.data
	msg		db		'Seconds since Jan 01 1970: ', 0h	; a message string

SECTION		.text
	global  _start

_start:
	mov		rax, msg	; move our message string into rax for printing
	call	sprint		; call our string printing function

	mov		rax, 201	; invoke SYS_TIME (kernel opcode 201)
	syscall

	call	iprintLF	; call our integer printing function with linefeed
	call	quit		; call our quit function
	