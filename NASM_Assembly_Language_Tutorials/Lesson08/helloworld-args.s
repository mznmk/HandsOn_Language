%include	'functions.s'

section		.text
	global	_start

_start:
	pop		rbx				; first value on the stack is the number of arguments

nextArg:
	cmp		rbx, 0h			; check to see if we have any arguments left
	jz		noMoreArgs		; if zero flag is set jump to noMoreArgs label (jumping over the end of the loop)

	pop		rax				; pop the next argument off the stack
	call	sprintLF		; call our print with linefeed function
	dec		rbx				; decrease rbx (number of arguments left) by 1
	jmp		nextArg			; jump to nextArg label

noMoreArgs:
	call	quit
