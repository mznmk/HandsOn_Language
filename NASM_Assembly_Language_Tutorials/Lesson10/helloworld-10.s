%include	'functions.s'

section		.text
	global	_start

_start:
	mov		rbx, 0			; rbx is initalised to zero.

nextNumber:
	inc		rbx				; increment rbx

	mov		rax, rbx		; move the address of our integer into rax
	add		rax, 48			; add 48 to our number to convert from integer to ascii for printing
	push	rax				; push rax to the stack
	mov		rax, rsp		; get the address of the character on the stack
	call	sprintLF		; call our print function

	pop		rax				; clean up the stack so we don't have unneeded bytes taking up space
	cmp		rbx, 10			; have we reached 10 yet? compare our counter with decimal 10
	jne		nextNumber		; jump if not equal and keep counting

	call	quit
