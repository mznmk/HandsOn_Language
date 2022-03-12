%include	'functions.s'										; include our external file

section		.data
	msg1	db		'Hello, brave new world!', 0h				; NOTE we have removed the line feed character 0Ah
	msg2	db		'This is how we recycle in NASM.', 0h		; NOTE we have removed the line feed character 0Ah

section		.text
	global	_start

_start:
	mov		rax, msg1
	call	sprintLF		 ;NOTE we are calling our new print with linefeed function

	mov		rax, msg2
	call	sprintLF		; NOTE we are calling our new print with linefeed function

	call	quit
