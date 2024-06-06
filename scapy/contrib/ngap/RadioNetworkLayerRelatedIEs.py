import common_types

# 9.3.1.2 Cause
causeGroup = {
    0 : "radio-network",
    1 : "transport",
    2 : "nas",
    3 : "protocol",
    4 : "misc"
}

causeRadioNetworkLayer = {
    0 : "unspecified",
	1 : "txnrelocoverall-expiry",
	2 : "successful-handover",
	3 : "release-due-to-ngran-generated-reason",
	4 : "release-due-to-5gc-generated-reason",
	5 : "handover-cancelled",	
	6 : "partial-handover",	
	7 : "ho-failure-in-target-5GC-ngran-node-or-target-system",
	8 : "ho-target-not-allowed",
	9 : "tngrelocoverall-expiry",
	10 : "tngrelocprep-expiry",
	11 : "cell-not-available",
	12 : "unknown-targetID",
	13 : "no-radio-resources-available-in-target-cell",
	14 : "unknown-local-UE-NGAP-ID",
	15 : "inconsistent-remote-UE-NGAP-ID",
	16 : "handover-desirable-for-radio-reason",
	17 : "time-critical-handover",
	18 : "resource-optimisation-handover",
	19 : "reduce-load-in-serving-cell",
	20 : "user-inactivity",
	21 : "radio-connection-with-ue-lost",
	22 : "radio-resources-not-available",
	23 : "invalid-qos-combination",
	24 : "failure-in-radio-interface-procedure",
	25 : "interaction-with-other-procedure",
	26 : "unknown-PDU-session-ID",
	27 : "unkown-qos-flow-ID",
	28 : "multiple-PDU-session-ID-instances",
	29 : "multiple-qos-flow-ID-instances",
	30 : "encryption-and-or-integrity-protection-algorithms-not-supported",
	31 : "ng-intra-system-handover-triggered",
	32 : "ng-inter-system-handover-triggered",
	33 : "xn-handover-triggered",
	34 : "not-supported-5QI-value",
	35 : "ue-context-transfer",
	36 : "ims-voice-eps-fallback-or-rat-fallback-triggered",
	37 : "up-integrity-protection-not-possible",
	38 : "up-confidentiality-protection-not-possible",
	39 : "slice-not-supported",
	40 : "ue-in-rrc-inactive-state-not-reachable",
	41 : "redirection",
	42 : "resources-not-available-for-the-slice",
	43 : "ue-max-integrity-protected-data-rate-reason",
	44 : "release-due-to-cn-detected-mobility",
	45 : "n26-interface-not-available",
	46 : "release-due-to-pre-emption",
	47 : "multiple-location-reporting-reference-ID-instances",
	48 : "rsn-not-available-for-the-up",
	49 : "npn-access-denied",
	50 : "cag-only-access-denied",
	51 : "insufficient-ue-capabilities",
	52 : "redcap-ue-not-supported",
	53 : "unknown-MBS-Session-ID",
	54 : "indicated-MBS-session-area-information-not-served-by-the-gNB",
	55 : "inconsistent-slice-info-for-the-session",
	56 : "misaligned-association-for-multicast-unicast"
}

causeTransportLayer = {
    0 : "transport-resource-unavailable",
	1 : "unspecified"
}

causeNAS = {
    0 : "normal-release",
	1 : "authentication-failure",
	2 : "deregister",
	3 : "unspecified",
	4 : "uE-not-in-PLMN-serving-area",
	5 : "mobile-IAB-not-authorized"
}

causeProtocol = {
    0: "transfer-syntax-error",
	1 : "abstract-syntax-error-reject",
	2 : "abstract-syntax-error-ignore-and-notify",
	3 : "message-not-compatible-with-receiver-state",
	4 : "semantic-error",
	5 : "abstract-syntax-error-falsely-constructed-message",
	6 : "unspecified"
}

causeMiscellaneous = {
    0 : "control-processing-overload",
	1 : "not-enough-user-plane-processing-resources",
	2 : "hardware-failure",
	3 : "om-intervention",
	4 : "unknown-PLMN-or-SNPN",
	5 : "unspecified"
}

# 9.3.1.5 Global RAN Node ID
NGRANNode = {
    0 : "gNB",
    1 : "ng-eNB",
    2 : "N3IWF",
    3 : "TNGF",
    4 : "TWIF",
    5 : "W-AGF"
}