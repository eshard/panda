#ifndef __SYSCALLS_HPP
#define __SYSCALLS_HPP

typedef struct CPUState CPUState;
typedef struct ReturnPoint ReturnPoint;

void syscall_return_switch_linux_arm ( CPUState *env, target_ulong pc, target_ulong ordinal, ReturnPoint &rp);
void syscall_return_switch_linux_x86 ( CPUState *env, target_ulong pc, target_ulong ordinal, ReturnPoint &rp);
void syscall_return_switch_windowsxp_sp2_x86 ( CPUState *env, target_ulong pc, target_ulong ordinal, ReturnPoint &rp);
void syscall_return_switch_windowsxp_sp3_x86 ( CPUState *env, target_ulong pc, target_ulong ordinal, ReturnPoint &rp);
void syscall_return_switch_windows7_x86 ( CPUState *env, target_ulong pc, target_ulong ordinal, ReturnPoint &rp);

void syscall_enter_switch_linux_arm ( CPUState *env, target_ulong pc );
void syscall_enter_switch_linux_x86 ( CPUState *env, target_ulong pc );
void syscall_enter_switch_windowsxp_sp2_x86 ( CPUState *env, target_ulong pc ) ;
void syscall_enter_switch_windowsxp_sp3_x86 ( CPUState *env, target_ulong pc ) ;
void syscall_enter_switch_windows7_x86 ( CPUState *env, target_ulong pc ) ;


void appendReturnPoint(ReturnPoint& rp);


#endif
