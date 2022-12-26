import Foundation

func getMachineHardwareName() -> String? {
    var sysInfo = utsname()
    let retVal = uname(&sysInfo)

    guard retVal == EXIT_SUCCESS else { return nil }

    return String(cString: &sysInfo.machine.0, encoding: .utf8)
}

print(getMachineHardwareName())


