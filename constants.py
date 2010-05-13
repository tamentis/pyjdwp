"""PyJDWP Constants."""

cmd_map = {
    "VM::Version":               (1, 1),
    "VM::ClassesBySignature":    (1, 2),
    "VM::AllClasses":            (1, 3),
    "VM::AllThreads":            (1, 4),
    "VM::TopLevelThreadGroups":  (1, 5),
    "VM::Dispose":               (1, 6),
    "VM::IDSizes":               (1, 7),
    "VM::Suspend":               (1, 8),
    "VM::Resume":                (1, 9),
    "VM::Exit":                  (1, 10),
    "VM::CreateString":          (1, 11),
    "VM::Capabilities":          (1, 12),
    "VM::ClassPaths":            (1, 13),
    "VM::DisposeObjects":        (1, 14),
    "VM::HoldEvents":            (1, 15),
    "VM::ReleaseEvents":         (1, 16),
    "VM::CapabilitiesNew":       (1, 17),
    "VM::RedefineClasses":       (1, 18),
    "VM::SetDefaultStratum":     (1, 19),
    "VM::AllClassesWithGeneric": (1, 20),
    "VM::InstanceCounts":        (1, 21),
    "EventRequest::Set":         (15, 1),
    "Event::Composite":          (64, 100),
}

jni_types = ("[", "L", "Z", "B", "C", "S", "I", "J", "F", "D")

# Errors Constants
NONE = 0
INVALID_THREAD = 10
INVALID_THREAD_GROUP = 11
INVALID_PRIORITY = 12
THREAD_NOT_SUSPENDED = 13
THREAD_SUSPENDED = 14
THREAD_NOT_ALIVE = 15
INVALID_OBJECT = 20
INVALID_CLASS = 21
CLASS_NOT_PREPARED = 22
INVALID_METHODID = 23
INVALID_LOCATION = 24
INVALID_FIELDID = 25
INVALID_FRAMEID = 30
NO_MORE_FRAMES = 31
OPAQUE_FRAME = 32
NOT_CURRENT_FRAME = 33
TYPE_MISMATCH = 34
INVALID_SLOT = 35
DUPLICATE = 40
NOT_FOUND = 41
INVALID_MONITOR = 50
NOT_MONITOR_OWNER = 51
INTERRUPT = 52
INVALID_CLASS_FORMAT = 60
CIRCULAR_CLASS_DEFINITION = 61
FAILS_VERIFICATION = 62
ADD_METHOD_NOT_IMPLEMENTED = 63
SCHEMA_CHANGE_NOT_IMPLEMENTED = 64
INVALID_TYPESTATE = 65
HIERARCHY_CHANGE_NOT_IMPLEMENTED = 66
DELETE_METHOD_NOT_IMPLEMENTED = 67
UNSUPPORTED_VERSION = 68
NAMES_DONT_MATCH = 69
CLASS_MODIFIERS_CHANGE_NOT_IMPLEMENTED = 70
METHOD_MODIFIERS_CHANGE_NOT_IMPLEMENTED = 71
NOT_IMPLEMENTED = 99
NULL_POINTER = 100
ABSENT_INFORMATION = 101
INVALID_EVENT_TYPE = 102
ILLEGAL_ARGUMENT = 103
OUT_OF_MEMORY = 110
ACCESS_DENIED = 111
VM_DEAD = 112
INTERNAL = 113
UNATTACHED_THREAD = 115
INVALID_TAG = 500
ALREADY_INVOKING = 502
INVALID_INDEX = 503
INVALID_LENGTH = 504
INVALID_STRING = 506
INVALID_CLASS_LOADER = 507
INVALID_ARRAY = 508
TRANSPORT_LOAD = 509
TRANSPORT_INIT = 510
NATIVE_METHOD = 511
INVALID_COUNT = 512

error_messages = {
    0: "No error has occurred.",
    10: "Passed thread is null, is not a valid thread or has exited.",
    11: "Thread group invalid.",
    12: "Invalid priority.",
    13: "If the specified thread has not been suspended by an event.",
    14: "Thread already suspended.",
    15: "Thread has not been started or is now dead.",
    20: "If this reference type has been unloaded and garbage collected.",
    21: "Invalid class.",
    22: "Class has been loaded but not yet prepared.",
    23: "Invalid method.",
    24: "Invalid location.",
    25: "Invalid field.",
    30: "Invalid jframeID.",
    31: "There are no more Java or JNI frames on the call stack.",
    32: "Information about the frame is not available.",
    33: "Operation can only be performed on current frame.",
    34: "The variable is not an appropriate type for the function used.",
    35: "Invalid slot.",
    40: "Item already set.",
    41: "Desired element not found.",
    50: "Invalid monitor.",
    51: "This thread doesn't own the monitor.",
    52: "The call has been interrupted before completion.",
    60: "The virtual machine attempted to read a class file and determined that the file is malformed or otherwise cannot be interpreted as a class file.",
    61: "A circularity has been detected while initializing a class.",
    62: "The verifier detected that a class file, though well formed, contained some sort of internal inconsistency or security problem.",
    63: "Adding methods has not been implemented.",
    64: "Schema change has not been implemented.",
    65: "The state of the thread has been modified, and is now inconsistent.",
    66: "A direct superclass is different for the new class version, or the set of directly implemented interfaces is different and canUnrestrictedlyRedefineClasses is false.",
    67: "The new class version does not declare a method declared in the old class version and canUnrestrictedlyRedefineClasses is false.",
    68: "A class file has a version number not supported by this VM.",
    69: "The class name defined in the new class file is different from the name in the old class object.",
    70: "The new class version has different modifiers and and canUnrestrictedlyRedefineClasses is false.",
    71: "A method in the new class version has different modifiers than its counterpart in the old class version and and canUnrestrictedlyRedefineClasses is false.",
    99: "The functionality is not implemented in this virtual machine.",
    100: "Invalid pointer.",
    101: "Desired information is not available.",
    102: "The specified event type id is not recognized.",
    103: "Illegal argument.",
    110: "The function needed to allocate memory and no more memory was available for allocation.",
    111: "Debugging has not been enabled in this virtual machine. JVMTI cannot be used.",
    112: "The virtual machine is not running.",
    113: "An unexpected internal error has occurred.",
    115: "The thread being used to call this function is not attached to the virtual machine. Calls must be made from attached threads.",
    500: "object type id or class tag.",
    502: "Previous invoke not complete.",
    503: "Index is invalid.",
    504: "The length is invalid.",
    506: "The string is invalid.",
    507: "The class loader is invalid.",
    508: "The array is invalid.",
    509: "Unable to load the transport.",
    510: "Unable to initialize the transport.",
    512: "The count is invalid.",
}
