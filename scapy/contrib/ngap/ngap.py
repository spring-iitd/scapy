# PDU Session Management Procedures 8.2
# PDU Session Resource Setup 8.2.1
class PDUSessionResourceSetupRequest:
    pass

class PDUSessionResourceSetupResponse:
    pass

# PDU Session Resource Release 8.2.2
class PDUSessionResourceReleaseCommand:
    pass

class PDUSessionResourceReleaseResponse:
    pass

# PDU Session Resource Modify 8.2.3
class PDUSessionResourceModifyRequest:
    pass

class PDUSessionResourceModifyResponse:
    pass

# PDU Session Resource Notify 8.2.4
class PDUSessionResourceNotify:
    pass

# PDU Session Resource Modify Indication 8.2.5
class PDUSessionResourceModifyIndication:
    pass

class PDUSessionResourceModifyConfirm:
    pass



# UE Context Management Procedures 8.3
# Initial Context Setup 8.3.1
class initialContextSetupRequest:
    pass

class initialContextSetupResponse:
    pass

class initialContextSetupFailure:
    pass


# UE Context Release Request (NG-RAN node initiated) 8.3.2
class UEContextReleaseRequest:
    pass


# UE Context Release (AMF initiated) 8.3.3
class UEContextReleaseCommand:
    pass

class UEContextReleaseComplete:
    pass

# UE Context Modification 8.3.4
class UEContextModificationRequest:
    pass

class UEContextModificationResponse:
    pass

class UEContextModificationFailure:
    pass


# RRC Inactive Transition Report 8.3.5
class RRCInactiveTransitionReport:
    pass


# Connection Establishment Indication 8.3.6
class connectionEstablishmentIndication:
    pass


# AMF CP Relocation Indication 8.3.7
class AMFCPRelocationIndication:
    pass


# RAN CP Relocation Indication 8.3.8
class RANCPRelocationIndication:
    pass


# Retrieve UE Information 8.3.9
class retrieveUEInformation:
    pass


# UE Information Transfer 8.3.10
class UEInformationTransfer:
    pass


# UE Context Suspend 8.3.11
class UEContextSuspendRequest:
    pass

class UEContextSuspendResponse:
    pass

class UEContextSuspendFailure:
    pass

# UE Context Resume 8.3.12
class UEContextResumeRequest:
    pass

class UEContextResumeResponse:
    pass

class UEContextResumeFailure:
    pass


# UE Mobility Management Messages 8.4
# Handover Preparation 8.4.1
class handoverRequired:
    pass

class handoverCommand:
    pass

# Handover Resource Allocation 8.4.2
class handoverRequest:
    pass

class handoverRequestAcknowledge:
    pass

# Handover Notification 8.4.3
class handoverNotify:
    pass

# Path Switch Request 8.4.4
class pathSwitchRequest:
    pass

class pathSwitchRequestAcknowledge:
    pass

class pathSwitchRequestFailure:
    pass

# Handover Cancellation 8.4.5
class handoverCancel:
    pass

class handoverAcknowledge:
    pass

# Uplink RAN Status Transfer 8.4.6
class uplinkRANStatusTransfer:
    pass

# Downlink RAN Status Transfer 8.4.7
class downlinkRANStatusTransfer:
    pass

# Handover Success 8.4.8
class handoverSuccess:
    pass

# Uplink RAN Early Status Transfer 8.4.9
class uplinkRANEarlyStatusTransfer:
    pass

# Downlink RAN Early Status Transfer
class downlinkRANEarlyStatusTransfer:
    pass



# Paging Procedures 8.5
# Paging 8.5.1
class paging:
    pass



# Transport of NAS Messages Procedures 8.6
# Initial UE Message 8.6.1
class initialUEMessage:
    pass

# Downlink NAS Transport 8.6.2
class downlinkNASTransport:
    pass

# Uplink NAS Transport 8.6.3
class uplinkNASTransport:
    pass

# NAS Non Delivery Indication 8.6.4
class NASNonDeliveryIndication:
    pass

# Reroute NAS Request 8.6.5
class rerouteNASRequest:
    pass



# Interface Management Messages 8.7
# NG Setup 8.7.1
class NGSetupRequest:
    pass
class NGSetupResponse:
    pass

class NGSetupFailure:
    pass

# RAN Configuration Update 8.7.2
class RANConfigurationUpdate:
    pass

class RANConfigurationUpdateAcknowledge:
    pass

class RANConfigurationUpdateFailure:
    pass

# AMF Configuration Update 8.7.3
class AMFConfigurationUpdate:
    pass

class AMFConfigurationUpdateAcknowledge:
    pass

class AMFConfigurationUpdateFailure:
    pass

# NG Reset 8.7.4
class NGReset:
    pass

class NGResetAcknowledge:
    pass

# Error Indication 8.7.5
class errorIndication:
    pass

# AMF Status Indication 8.7.6
class AMFStatusIndication:
    pass

# Overload Start 8.7.7
class overloadStart:
    pass

# Overload Stop 8.7.8
class overloadStop:
    pass



# Configuration Transfer Procedures 8.8
# uplinkRANConfigurationTransfer 8.8.1
class uplinkRANConfigurationTransfer:
    pass

# Downlink RAN Configuration Transfer 8.8.2
class downlinkRANConfigurationTransfer:
    pass



# Warning Message Transmission Procedures 8.9
# Write-Replace Warning 8.9.1
class writeReplaceWarningRequest:
    pass

class writeReplaceWarningResponse:
    pass

# PWS Cancel 8.9.2
class PWSCancelRequest:
    pass

class PWSCancelResponse:
    pass

# PWS Restart Indication 8.9.3
class PWSRestartIndication:
    pass

# PWS Failure Indication 8.9.4
class PWSFailureIndication:
    pass



# NRPPa Transport Procedures 8.10
class downlinkUEAssociatedNRPPATransport:
    pass

class UplinkUEAssociatedNRPPATransport:
    pass

class downlinkNonUEAssociatedNRPPATransport:
    pass

class UplinkNonUEAssociatedNRPPATransport:
    pass



# Trace Procedures 8.11
# Trace Start 8.11.1
class traceStart:
    pass

# Trace Failure Indication 8.11.2
class traceFailureIndication:
    pass

# Deactivate Trace 8.11.3
class deactivateTrace:
    pass

# Cell Traffic Trace 8.11.4
class cellTraficTrace:
    pass



# Location Reporting Procedures 8.12
# Location Reporting Control 8.12.1
class locationReportingControl:
    pass

# Location Reporting Failure Indication 8.12.2
class locationReportingFailureIndication:
    pass

# Location Report 8.12.3
class locationReport:
    pass



# UE TNLA Binding Procedures 8.13
# UE TNLA Binding Release 8.13.1
class UETNLABindingReleaseRequest:
    pass



# UE Radio Capability Management Procedures 8.14
# UE Radio Capability Info Indication 8.14.1
class UERadioCapabilityInfoIndication:
    pass

# UE Radio Capability Check 8.14.2
class UERadioCapabilityCheckRequest:
    pass

class UERadioCapabilityCheckResponse:
    pass

# UE Radio Capability ID Mapping
class UERadioCapabilityIDMappingRequest:
    pass

class UERadioCapabilityIDMappingResponse:
    pass



# Data Usage Reporting Procedures 8.15
# Secondary RAT Data Usage Report 8.15.1
class secondaryRATDataUsageReport:
    pass

# RIM Information Transfer Procedures 8.16
# Uplink RIM Information Transfer 8.16.1
class uplinkRIMInformationTransfer:
    pass

# Downlink RIM Information Transfer 8.16.2
class downlinkRIMInformationTransfer:
    pass
