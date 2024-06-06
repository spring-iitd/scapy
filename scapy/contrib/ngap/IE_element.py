import common_types
import RadioNetworkLayerRelatedIEs


# Radio Network Layer Related IEs
# 9.3.1.1 Message Type
class IEMessageType(Packet):
    name="Message Type"
    fields_desc = [
        ByteField("Procedure Code"),
        ByteEnumField("Type of Message", 0, common_types.TriggeringMessage)
    ]
    

# 9.3.1.2 Cause
class IECause(Packet):
    name="Cause"
    fields_desc = [
        BytesEnumField("Cause", 0, RadioNetworkLayerRelatedIEs.causeGroup),
        ConditionalField(ByteEnumField("Radio Network Layer Cause", 0, RadioNetworkLayerRelatedIEs.causeRadioNetworkLayer), lambda pkt:pkt.Cause == 0),
        ConditionalField(ByteEnumField("Transport Layer Cause", 1, RadioNetworkLayerRelatedIEs.causeTransport), lambda pkt:pkt.Cause == 1),
        ConditionalField(ByteEnumField("NAS Cause", 3, RadioNetworkLayerRelatedIEs.causeNAS), lambda pkt:pkt.Cause == 2),
        ConditionalField(ByteEnumField("Protocol Cause", 6, RadioNetworkLayerRelatedIEs.causeProtocol), lambda pkt:pkt.Cause == 3),
        ConditionalField(ByteEnumField("Miscellaneous Cause", 5, RadioNetworkLayerRelatedIEs.causeMisc), lambda pkt:pkt.Cause == 4)
    ]
    

# 9.3.1.3 Criticality Diagnostics
class IECriticalityDiagnostics(Packet):
    name="Criticality Diagnostics"
    fields_desc = [
        ConditionalField(ByteField("Procedure Code", 0), lambda pkt:pkt.ProcedureCodePresent),
        ConditionalField(ByteEnumField("Triggering Message", 0, common_types.TriggeringMessage), lambda pkt:pkt.TriggeringMessagePresent),
        ConditionalField(ByteEnumField("Procedure Criticality", 0, common_types.Criticality), lambda pkt:pkt.ProcedureCriticalityPresent),
    
    ]

# 9.3.1.4 Bit Rate
class IEBitRate(Packet):
    name="Bit Rate"
    fields_desc = [IntField("Bit Rate")]

# 9.3.1.5 Global RAN Node ID
class IEGlobalRANNodeID(Packet):
    name="Global RAN Node ID"
    fields_desc = [
        ByteEnumField("NG-RAN node", 0, RadioNetworkLayerRelatedIEs.NGRANNode),
        ConditionalField(IEGlobalRANNodeID, lambda pkt:pkt.NGRANNode == 0),
        ConditionalField(GlobalngeNBID, lambda pkt:pkt.NGRANNode == 1),
        ConditionalField(GlobalN3IWFID, lambda pkt:pkt.NGRANNode == 2),
        ConditionalField(GlobalTNGF, lambda pkt:pkt.NGRANNode == 3),
        ConditionalField(GlobalTWIFID, lambda pkt:pkt.NGRANNode == 4),
        ConditionalField(GlobalW_AGFID, lambda pkt:pkt.NGRANNode == 5)
    ]

# 9.3.1.6 Global gNB ID
class IEGlobalgNBID(Packet):
    name="Global gNB ID"
    fields_desc = []
    pass

# 9.3.1.7 NR CGI
class IENRCGI(Packet):
    name="NR CGI"
    fields_desc = []
    pass

# 9.3.1.8 Global ng-eNB ID
class IEGlobalngeNBID(Packet):
    name="Global ng-eNB ID"
    fields_desc = []
    pass

# 9.3.1.9 E-UTRA CGI
class IEEUTRACGI(Packet):
    name="E-UTRA CGI"
    fields_desc = []
    pass

# 9.3.1.10 GBR QoS Flow Information
class IEGBRQoSFlowInformation(Packet):
    name="GBR QoS Flow Information"
    fields_desc = []
    pass

# 9.3.1.12 QoS Flow Level QoS Parameters
class IEQoSFlowLevelQoSParameters(Packet):
    name="QoS FLow Level QoS Parameters"
    fields_desc = []
    pass

# 9.3.1.13 QoS Flow List with Cause 
class IEQoSFlowListwithCause(Packet):
    name="QoS Flow List with Cause"
    fields_desc = []
    pass

# 9.3.1.14 Trace Activation
class IETraceActivation(Packet):
    name="Trace Activation"
    fields_desc = []
    pass

# 9.3.1.15 Core Network Assistance Information for RRC INACTIVE
class IECoreNetworkAssistanceInfoforRRCINACTIVE(Packet):
    name="Core Network Assistance Information for RRC INACTIVE"
    fields_desc = []
    pass

# 9.3.1.16 User Location Information
class IEUserLocationInformation(Packet):
    name="User Location Information"
    fields_desc = []
    pass

# 9.3.1.17 Slice Support List
class IESliceSupportList(Packet):
    name="Slice Support List"
    fields_desc = []
    pass

# 9.3.1.18 Dynamic 5QI Descriptor
class IEDynamic5QIDescriptor(Packet):
    name="Dynamic 5QI Descriptor"
    fields_desc = []
    pass

# 9.3.1.19 Allocation and Retention Policy 
class IEAllocationandRetentionPolicy(Packet):
    name="Allocation and Retention Policy"
    fields_desc = []
    pass

# 9.3.1.20 Source to Target Transport Container
class IESourcetoTargetTransportContainer(Packet):
    name="Source to Target Transport Container"
    fields_desc = []
    pass

# 9.3.1.21 Target to Source Transparent Container
class IETargettoSourceTransparentContainer(Packet):
    name="Target to Source Transparent Container"
    fields_desc = []
    pass

# 9.3.1.22 Handover Type
class IEHandoverType(Packet):
    name="Handover Type"
    fields_desc = []
    pass

# 9.3.1.23 MICO Mode Indication
class IEMICOModeIndication(Packet):
    name="MICO Mode Indication"
    fields_desc = []
    pass

# 9.3.1.24 S-NSSAI
class IES_NSSAI(Packet):
    name="S-NSSAI"
    fields_desc = []
    pass

# 9.3.1.25 Target ID
class IETargetID(Packet):
    name="Target ID"
    pass

# 9.3.1.26 Emergency Fallback Indicator
class IEEmergencyFallbackIndicator(Packet):
    name="Emergency Fallback Indicator"
    fields_desc = []
    pass

# 9.3.1.27 Security Indication
class IESecurityIndication(Packet):
    name="Security Indication"
    fields_desc = []
    pass

# 9.3.1.28 Non Dynamic 5QI Descriptor
class IENonDynamic5QIDescriptor(Packet):
    name="Non Dynamic 5QI Descriptor"
    fields_desc = []
    pass

# 9.3.1.29 Source NG-RAN Node to Target NG-RAN Node Transparent Container
class IESourceNG_RANNodetoTargetNG_RANNodeTransparentContainer(Packet):
    name="Source NG-RAN Node to target NG-RAN Node Transparent Container"
    fields_desc = []
    pass

# 9.3.1.30 Target NG-RAN Node to Source NG-RAN Node Transparent Container
class IETargetNG_RANNodetoSourceNG_RANNodeTransparentContainer(Packet):
    name="Target NG-RAN Node to Source NG-RAN Node Transparent Container"
    fields_desc = []
    pass

# 9.3.1.31 Allowed NSSAI
class IEAllowedNSSAI(Packet):
    name="Allowed NSSAI"
    fields_desc = []
    pass

# 9.3.1.32 Relative AMF Capacity
class IERelativeAMFCapacity(Packet):
    name="Relative AMF Capacity"
    fields_desc = []
    pass

# 9.3.1.33 DL Forwarding
class IEDLForwarding(Packet):
    name="DL Forwarding"
    fields_desc = []
    pass

# 9.3.1.34 DRBs to QoS Flows Mapping List
class IEDRBstoQoSFlowsMappingList(Packet):
    name="DRBs to QoS Flows Mapping List"
    fields_desc = []
    pass

# 9.3.1.35 Message Identifier
class IEMessageIdentifier(Packet):
    name="Message Identifier"
    fields_desc = []
    pass

# 9.3.1.36 Serial Number
class IESerialNumber(Packet):
    name="Serial Number"
    fields_desc = []
    pass

# 9.3.1.37 Warning Area List
class IEWarningAreaList(Packet):
    name="Warning Area List"
    fields_desc = []
    pass

# 9.3.1.38 Number of Broadcasts Requested
class IENumberofBroadcastsRequested(Packet):
    name="Number of Broadcasts Requested"
    fields_desc = []
    pass

# 9.3.1.39 Warning Type
class IEWarningType(Packet):
    name="Warning Type"
    fields_desc = []
    pass

# 9.3.1.41 Data Coding Scheme
class IEDataCodingScheme(Packet):
    name="Data Coding Scheme"
    fields_desc = []
    pass

# 9.3.1.42 Warning Message Contents
class IEWarningMessageContents(Packet):
    name="Warning Message Contents"
    fields_desc = []
    pass

# 9.3.1.43 Broadcast Completed Area List
class IEBroadcastCompletedAreaList(Packet):
    name="Broadcast Completed Area List"
    fields_desc = []
    pass

# 9.3.1.44 Broadcast Cancelled Area List
class IEBroadcastCancelledAreaList(Packet):
    name="Broadcast Cancelled Area List"
    fields_desc = []
    pass

# 9.3.1.45 Number of Broadcasts
class IENumberofBroadcasts(Packet):
    name="Number of Broadcasts"
    fields_desc = []
    pass

# 9.3.1.46 Concurrent Warning Message Indicator
class IEConcurrentWarningMessageIndicator(Packet):
    name="Concurrent Warning Message Indicator"
    fields_desc = []
    pass

# 9.3.1.47 Cancel-All Warning Messages Indicator
class IECancel_AllWarningMessagesIndicator(Packet):
    name="Cancel-All Warning Message Indicator"
    fields_desc = []
    pass

# 9.3.1.48 Emergency Area ID
class IEEmergencyAreaID(Packet):
    name="Emergency Area ID"
    fields_desc = []
    pass

# 9.3.1.49 Repetition Period
class IERepetitionPeriod(Packet):
    name="Repetition Period"
    fields_desc = []
    pass

# 9.3.1.50 PDU Session ID
class IEPDUSessionID(Packet):
    name="PDU Session ID"
    fields_desc = []
    pass

# 9.3.1.51 QoS Flow Identifier
class IEQoSFlowIdentifier(Packet):
    name="QoS Flow Identifier"
    fields_desc = []
    pass

# 9.3.1.52 PDU Session Type
class IEPDUSessionType(Packet):
    name="PDU Session Type"
    fields_desc = []
    pass

# 9.3.1.53 DRB ID
class IEDRBID(Packet):
    name="DRB ID"
    fields_desc = []
    pass

# 9.3.1.54 Masked IMEISV
class IEMaskedIMEISV(Packet):
    name="Masked IMEISV"
    fields_desc = []
    pass

# 9.3.1.55 New Security Context Indicator
class IENewSecurityContextIndicator(Packet):
    name="New Security Context Indicator"
    fields_desc = []
    pass

# 9.3.1.56 Time to Wait
class IETimetoWait(Packet):
    name="Time to Wait"
    fields_desc = []
    pass

# 9.3.1.57 Global N3IWF ID
class IEGlobalN3IWFID(Packet):
    name="Global N3IWF ID"
    fields_desc = []
    pass

# 9.3.1.58 UE Aggregate Maximum Bit Rate
class IEUEAggregateMaximumBitRate(Packet):
    name="UE Aggregate Maximum Bit Rate"
    fields_desc = []
    pass

# 9.3.1.59 Security Result
class IESecurityResult(Packet):
    name="Security Result"
    fields_desc = []
    pass

# 9.3.1.60 User Plane Security Information
class IEUserPlaneSecurityInformation(Packet):
    name="User Plane Security Information"
    fields_desc = []
    pass

# 9.3.1.61 Index to RAT/Frequency Selection Priority
class IEIndextoRATorFrequencySelectionPriority(Packet):
    name="Index to RAT/Frequency Selection Priority"
    fields_desc = []
    pass

# 9.3.1.62 Data Forwarding Accepted
class IEDataForwardingAccepted(Packet):
    name="Data Forwarding Accepted"
    fields_desc = []
    pass

# 9.3.1.63 Data Forwarding Not Possible
class IEDataForwardingNotPossible(Packet):
    name="Data Forwarding Not Possible"
    fields_desc = []
    pass

# 9.3.1.64 Direct Forwarding Path Availability
class IEDirectForwardingPathAvailability(Packet):
    name="Direct Forwarding Path Availablility"
    fields_desc = []
    pass

# 9.3.1.65 Location Reporting Request Type
class IELocationReportingRequestType(Packet):
    name="Location Reporting Request Type"
    fields_desc = []
    pass

# 9.3.1.66 Area of Interest
class IEAreaofInterest(Packet):
    name="Area of Interest"
    fields_desc = []
    pass

# 9.3.1.67 UE Presence in Area of Interest List
class IEUEPresenceinAreaofInterestList(Packet):
    name="UE Presence in Area of Interest List"
    fields_desc = []
    pass

# 9.3.1.68 UE Radio Capability for Paging
class IEUERadioCapabilityforPaging(Packet):
    name="UE Radio Capability for Paging"
    fields_desc = []
    pass

# 9.3.1.69 Assistance Data for Paging
class IEAssistanceDataforPaging(Packet):
    name="Assistance Data for Paging"
    fields_desc = []
    pass

# 9.3.1.70 Assistance Data for Recommended Cells
class IEAssistanceDataforRecommendedCells(Packet):
    name="Assistance Data for Recommended Calls"
    fields_desc = []
    pass

# 9.3.1.71 Recommended Cells for Paging
class IERecommendedCellsforPaging(Packet):
    name="Recommmended Cells for Paging"
    fields_desc = []
    pass

# 9.3.1.72 Paging Attempt Information
class IEPagingAttemptInformation(Packet):
    name="Paging Attempt Information"
    fields_desc = []
    pass

# 9.3.1.73 NG-RAN CGI
class IENG_RANCGI(Packet):
    name="NG-RAN CGI"
    fields_desc = []
    pass

# 9.3.1.74 UE Radio Capability
class IEUERadioCapability(Packet):
    name="UE Radio Capability"
    fields_desc = []
    pass

# 9.3.1.74a UE Radio Capability - E-UTRA Format
class IEUERadioCapability_E_UTRAFormat(Packet):
    name="UE Radio Capability - E-UTRA format"
    fields_desc = []
    pass

# 9.3.1.75 Time Stamp
class IETimeStamp(Packet):
    name="Time Stamp"
    fields_desc = []
    pass

# 9.3.1.76 Location Reporting Reference ID
class IELocationReportingReferenceID(Packet):
    name="Location Reporting Reference ID"
    fields_desc = []
    pass

# 9.3.1.77 Data Forwarding Response DRB List
class IEDataForwardingResponseDRBList(Packet):
    name="Data Forwarding Response DRB List"
    fields_desc = []
    pass

# 9.3.1.78 Paging Priority
class IEPagingPriority(Packet):
    name="Paging Priority"
    fields_desc = []
    pass

# 9.3.1.79 Packet Loss Rate
class IEPacketLossRate(Packet):
    name="Packet Loss Rate"
    fields_desc = []
    pass

# 9.3.1.80 Packet Delay Budget
class IEPacketDelayBudget(Packet):
    name="Packet Delay Budget"
    fields_desc = []
    pass

# 9.3.1.81 Packet Error Rate
class IEPacketErrorRate(Packet):
    name="Packet Error Rate"
    fields_desc = []
    pass

# 9.3.1.82 Averaging Window
class IEAveragingWindow(Packet):
    name="Averging Window"
    fields_desc = []
    pass

# 9.3.1.83 Maximum Data Burst Volume
class IEMaximumDataBurstVolume(Packet):
    name="Maximum Data Burst Volume"
    fields_desc = []
    pass

# 9.3.1.84 Priority Level
class IEPriorityLevel(Packet):
    name="Priority Level"
    fields_desc = []
    pass

# 9.3.1.85 Mobility Restriction List
class IEMobilityRestrictionList(Packet):
    name="Mobility Restriction List"
    fields_desc = []
    pass

# 9.3.1.86 UE Security Capabilities
class IEUESecurityCapabilities(Packet):
    name="UE Security Capabilities"
    fields_desc = []
    pass

# 9.3.1.87 Security Key
class IESecurityKey(Packet):
    name="Security Key"
    fields_desc = []
    pass

# 9.3.1.88 Security Context
class IESecurityContext(Packet):
    name="Security Context"
    fields_desc = []
    pass

# 9.3.1.89 IMS Voice Support Indicator
class IEIMSVoiceSupportIndicator(Packet):
    name="IMS Voice Support Indicator"
    fields_desc = []
    pass

# 9.3.1.90 Paging DRX
class IEPagingDRX(Packet):
    name="Paging DRX"
    fields_desc = []
    pass

# 9.3.1.91 RRC Inactive Transition Report Request 
class IERRCInactiveTransitionReportRequest(Packet):
    name="RRC Inactive Transition Report Request"
    fields_desc = []
    pass

# 9.3.1.92 RRC State
class IERRCState(Packet):
    name="RRC State"
    fields_desc = []
    pass

# 9.3.1.93 Expected UE Behaviour
class IEExpectedUEBehaviour(Packet):
    name="Expected UE Behaviour"
    fields_desc = []
    pass

# 9.3.1.94 Expected UE Activity Behaviour
class IEExpectedUEActivityBehaviour(Packet):
    name="Expected UE Activity Behaviour"
    fields_desc = []
    pass

# 9.3.1.95 UE History Information
class IEUEHistoryInformation(Packet):
    name="UE History Information"
    fields_desc = []
    pass

# 9.3.1.96 Last Visited Cell Information
class IELastVisitedCellInformation(Packet):
    name="Last Visited Cell Information"
    fields_desc = []
    pass

# 9.3.1.97 Last Visited NG-RAN Cell Information
class IELastVisitedNG_RANCellInformation(Packet):
    name="Last Visited NG-RAN Cell Information"
    fields_desc = []
    pass

# 9.3.1.98 Cell Type
class IECellType(Packet):
    name="Cell Type"
    fields_desc = []
    pass

# 9.3.1.99 Associated QoS Flow List
class IEAssociatedQoSFlowList(Packet):
    name="Associtated QoS Flow List"
    fields_desc = []
    pass

# 9.3.1.100 Information on Recommended Cells and RAN Nodes for Paging
class IEInformationonRecommendedCellsandRANNodesforPaging(Packet):
    name="Information on Recommended Cells and RAN Nodes for Paging"
    fields_desc = []
    pass

# 9.3.1.101 Recommended RAN Nodes for Paging
class IERecommendedRANNodesforPaging(Packet):
    name="Recommended RAN Nodes for Paging"
    fields_desc = []
    pass

# 9.3.1.102 PDU Session Aggregate Maximum Bit Rate
class IEPDUSessionAggregateMaximumBitRate(Packet):
    name="PDU Session Aggregate Maximum Bit Rate"
    fields_desc = []
    pass

# 9.3.1.103 Maximum Integrity Protected Data Rate
class IEMaximumIntegrityProtectedDataRate(Packet):
    name="Maximum Integrity Protected Data Rate"
    fields_desc = []
    pass

# 9.3.1.104 Overload Response
class IEOverloadResponse(Packet):
    name="Overload Response"
    fields_desc = []
    pass

# 9.3.1.105 Overload Action
class IEOverloadAction(Packet):
    name="Overload Action"
    fields_desc = []
    pass

# 9.3.1.106 Traffic Load Reduction Indication
class IETrafficLoadReductionIndication(Packet):
    name="Traffic Load Reduction Indication"
    fields_desc = []
    pass

# 9.3.1.107 Slice Overload List
class IESliceOverloadList(Packet):
    name="Slice Overload List"
    fields_desc = []
    pass

# 9.3.1.108 RAN Status Transfer Transparent Container
class IERANStatusTransferTransparentContainer(Packet):
    name="RAN Status Transfer Transparent Container"
    fields_desc = []
    pass

# 9.3.1.109 COUNT Value for PDCP SN Length 12
class IECOUNTValueforPDCPSNLength12(Packet):
    name="COUNT Value for PDCP SN Length 12"
    fields_desc = []
    pass

d# 9.3.1.110 COUNT Value for PDCP SN Length 18
class IECOUNTValueforPDCPSNLength18(Packet):
    name="COUNT Value for PDCP SN Length 18"
    fields_desc = []
    pass

# 9.3.1.111 RRC Establishment Cause
class IERRCEstablishmentCause(Packet):
    name="RRC Establishment Cause"
    fields_desc = []
    pass

# 9.3.1.112 Warning Area Coordinates
class IEWarningAreaCoordinates(Packet):
    name="Warning Area Coordinates"
    fields_desc = []
    pass

# 9.3.1.113 Network Instance
class IENetworkInstance(Packet):
    name="Network Instance"
    fields_desc = []
    pass

# 9.3.1.114 Secondary RAT Usage Information
class IESecondaryRATUsageInformation(Packet):
    name="Secondary RAT Usage Information"
    fields_desc = []
    pass


# 9.3.1.115 Volume Timed Report List
class IEVolumeTimedReportList(Packet):
    name="Volume Timed Report List"
    fields_desc = []
    pass

# 9.3.1.116 Redirection for Voice EPS Fallback
class IERedirectionforVoiceEPSFallback(Packet):
    name="Redirection for Voice EPS Fallback"
    fields_desc = []
    pass

# 9.3.1.117 UE Retention Information
class IEUERetentionInformation(Packet):
    name="UE Retention Information"
    fields_desc = []
    pass

# 9.3.1.118 UL Forwarding
class IEULForwarding(Packet):
    name="UL Forwarding"
    fields_desc = []
    pass

# 9.3.1.119 CN Assisted RAN Parameters Tuning
class IECNAssistedRANParametersTuning(Packet):
    name="CN Assisted RAN Parameters Tuning"
    fields_desc = []
    pass

# 9.3.1.120 Common Network Instance
class IECommonNetworkInstance(Packet):
    name="Common Network Instance"
    fields_desc = []
    pass

# 9.3.1.121 Data Forwarding Response E-RAB List
class IEDataForwardingResponseE_RABList(Packet):
    name="Data Forwarding Response E-RAB List"
    fields_desc = []
    pass

# 9.3.1.122 gNB Set ID
class IEgNBSetID(Packet):
    name="gNB Set ID"
    fields_desc = []
    pass

# 9.3.1.123 RNC-ID
class IERNC_ID(Packet):
    name="RNC-ID"
    fields_desc = []
    pass

# 9.3.1.124 Extended RNC-ID
class IEExtendedRNC_ID(Packet):
    name="Extended RNC-ID"
    fields_desc = []
    pass

# 9.3.1.125 RAT Information
class IERATInformation(Packet):
    name="RAT Information"
    fields_desc = []
    pass

# 9.3.1.126 Extended RAT Restriction Information
class IEExtendedRATRestrictionInformation(Packet):
    name="Extended RAT Restriction Information"
    fields_desc = []
    pass

# 9.3.1.127 SgNB UE X2AP ID
class IESgNBUEX2APID(Packet):
    name="SgNB UE X2AP ID"
    fields_desc = []
    pass

# 9.3.1.128 SRVCC Operation Possible 
class IESRVCCOperationPossible(Packet):
    name="SRVCC Operation Possible"
    fields_desc = []
    pass

# 9.3.1.129 IAB Authorized
class IEIABAuthorized(Packet):
    name="IAB Authorized"
    fields_desc = []
    pass

# 9.3.1.130 TSC Traffic Characteristics
class IETSCTrafficCharacteristics(Packet):
    name="TSC Traffic Characteristics"
    fields_desc = []
    pass

# 9.3.1.131 TSC Assistance Information
class IETSCAssistanceInformation(Packet):
    name="TSC Assistance Information"
    fields_desc = []
    pass

# 9.3.1.132 Periodicity
class IEPeriodicity(Packet):
    name="Periodicity"
    fields_desc = []
    pass

# 9.3.1.133 Burst Arrival Time
class IEBurstArrivalTime(Packet):
    name="Burst Arrival Time"
    fields_desc = []
    pass

# 9.3.1.134 Redundant QoS Flow Indicator
class IERedundantQoSFlowIndicator(Packet):
    name="Redundant QoS Flow Indicator"
    fields_desc = []
    pass

# 9.3.1.135 Extended Packet Delay Budget
class IEExtendedPacketDelayBudget(Packet):
    name="Extended Packet Delay Budget"
    fields_desc = []
    pass

# 9.3.1.136 Redundant PDU Session Information
class IERedundantPDUSessionInformation(Packet):
    name="Redundant PDU Session Information"
    fields_desc = []
    pass

# 9.3.1.137 NB-IoT Default Paging DRX
class IENB_IoTDefaultPagingDRX(Packet):
    name="NB-IoT Default Paging DRX"
    fields_desc = []
    pass

# 9.3.1.138 NB-IoT Paging eDRX Information
class IENB_IoTPagingeDRXInformation(Packet):
    name="NB-IoT Paging eDRX Information"
    fields_desc = []
    pass

# 9.3.1.139 NB-IoT Paging DRX
class IENB_IoTPagingDRX(Packet):
    name="NB-IoT Paging DRX"
    fields_desc = []
    pass

# 9.3.1.140 Enhanced Coverage Restriction
class IEEnhancedCoverageRestriction(Packet):
    name="Enhanced Coverage Restriction"
    fields_desc = []
    pass

# 9.3.1.141 Paging Assistance Data for CE Capable UE
class IEPagingAssistanceDataforCECapableUE(Packet):
    name="Paging Assistance Data for CE Capable UE"
    fields_desc = []
    pass

# 9.3.1.142 UE Radio Capability ID
class IEUERadioCapabilityID(Packet):
    name="UE Radio Capability ID"
    fields_desc = []
    pass

# 9.3.1.143 WUS Assistance Information
class IEWUSAssistanceInformation(Packet):
    name="WUS Assistance Information"
    fields_desc = []
    pass

# 9.3.1.144 UE Differentiation Information
class IEUEDifferentiationInformation(Packet):
    name="UE Differentiation Information"
    fields_desc = []
    pass

# 9.3.1.145 NB-IoT UE Priority
class IENB_IoTUEPriority(Packet):
    name="NB-IoT UE Priority"
    fields_desc = []
    pass

# 9.3.1.146 NR V2X Services Authorized
class IENRV2XServicesAuthorized(Packet):
    name="NR V2X Services Authorized"
    fields_desc = []
    pass

# 9.3.1.147 LTE V2X Services Authorized
class IELTEV2XServicesAuthorized(Packet):
    name="LTE V2X Services Authorized"
    fields_desc = []
    pass

# 9.3.1.148 NR UE Sidelink Aggregate Maximum Bit Rate
class IENRUESidelinkAggregateMaximumBitRate(Packet):
    name="NR UE Sidelink Aggregate Maximum Bit Rate"
    fields_desc = []
    pass

# 9.3.1.149 LTE UE Sidelink Aggregate Maximum Bit Rate
class IELTEUESidelinkAggregateMaximumBitRate(Packet):
    name="LTE UE Sidelink Aggregate Maximum Bit Rate"
    fields_desc = []
    pass

# 9.3.1.150 PC5 QoS Parameters
class IEPC5QoSParameters(Packet):
    name="PC5 QoS Parameters"
    fields_desc = []
    pass

# 9.3.1.151 Alternative QoS Parameters Set List
class IEAlternativeQoSParametersSetList(Packet):
    name="ALternative QoS Parameters Set List"
    fields_desc = []
    pass

# 9.3.1.152 Alternative QoS Parameters Set Index
class IEAlternativeQoSParametersSetIndex(Packet):
    name="Alternative QoS Parameters Set Index"
    fields_desc = []
    pass

# 9.3.1.153 Alternative QoS Parameters Set Notify Index
class IEAlternativeQoSParametersSetNotifyIndex(Packet):
    name="Alternative QoS Parameters Set Notify Index"
    fields_desc = []
    pass

# 9.3.1.154 Paging eDRX Information
class IEPagingeDRXInformation(Packet):
    name="Paging eDRX Information"
    fields_desc = []
    pass

# 9.3.1.155 CE-mode-B Restricted
class IECE_mode_BRestricted(Packet):
    name="CE-mode-B Restricted"
    fields_desc = []
    pass

# 9.3.1.156 CE-mode-B Support Indicator
class IECE_mode_BSupportIndicator(Packet):
    name="CE-mode-B Support Indicator"
    fields_desc = []
    pass

# 9.3.1.157 LTE-M Indication
class IELTE_MIndication(Packet):
    name="LTE-M Indication"
    fields_desc = []
    pass

# 9.3.1.158 Suspend Request Indication
class IESuspendRequestIndication(Packet):
    name="Suspend Request Indication"
    fields_desc = []
    pass

# 9.3.1.159 Suspend Response Indication
class IESuspendResponseIndication(Packet):
    name="Suspend Response Indication"
    fields_desc = []
    pass

# 9.3.1.160 UE User Plane CIoT Support Indicator
class IEUEUserPlaneCIoTSupportIndicator(Packet):
    name="UE User Plane CIoT Support Indicator"
    fields_desc = []
    pass

# 9.3.1.161 Global TNGF ID
class IEGlobalTNGFID(Packet):
    name="Global TNGF ID"
    fields_desc = []
    pass

# 9.3.1.162 Global W-AGF ID
class IEGlobalW_AGFID(Packet):
    name="Global W-AGF ID"
    fields_desc = []
    pass

# 9.3.1.163 Global TWIF ID
class IEGlobalTWIFID(Packet):
    name="Global TWIF ID"
    fields_desc = []
    pass

# 9.3.1.164 W-AGF User Location Information
class IEW_AGFUserLocationInformation(Packet):
    name="W-AGF User Location Information"
    fields_desc = []
    pass

# 9.3.1.165 Global eNB ID
class IEGlobaleNBID(Packet):
    name="Global eNB ID"
    fields_desc = []
    pass

# 9.3.1.166 UE History Information from UE
class IEUEHistoryInformationfromUE(Packet):
    name="UE History Information from UE"
    pass

# 9.3.1.167 MDT Configuration
class IEMDTConfiguration(Packet):
    name="MDT Configuration"
    fields_desc = []
    pass

# 9.3.1.168 MDT PLMN List
class IEMDTPLMNList(Packet):
    name="MDT PLMN List"
    fields_desc = []
    pass

# 9.3.1.169 MDT Configuration-NR
class IEMDTConfiguration_NR(Packet):
    name="MDT Configuration-NR"
    fields_desc = []
    pass

# 9.3.1.170 MDT Configuration-EUTRA
class IEMDTConfiguration_EUTRA(Packet):
    name="MDT Configuration-EUTRA"
    fields_desc = []
    pass

# 9.3.1.171 M1 Configuration
class IEM1Configuration(Packet):
    name="M1 Configuration"
    fields_desc = []
    pass

# 9.3.1.172 M4 Configuration
class IEM4Configuration(Packet):
    name="M4 Configuration"
    fields_desc = []
    pass

# 9.3.1.173 M5 Configuration
class IEM5Configuration(Packet):
    name="M5 Configuration"
    fields_desc = []
    pass

# 9.3.1.174 M6 Configuration
class IEM6Configuration(Packet):
    name="M6 Configuration"
    fields_desc = []
    pass

# 9.3.1.175 M7 Configuration
class IEM7Configuration(Packet):
    name="M7 Configuration"
    fields_desc = []
    pass

# 9.3.1.176 MDT Location Information
class IEMDTLocationInformation(Packet):
    name="MDT Location Information"
    fields_desc = []
    pass

# 9.3.1.177 Bluetooth Measurement Configuration
class IEBluetoothMeasurementConfiguration(Packet):
    name="Bluetooth Measurement Configuration"
    fields_desc = []
    pass

# 9.3.1.178 WLAN Measurement Configuration
class IEWLANMeasurementConfiguration(Packet):
    name="WLAN Measurement Configuration"
    fields_desc = []
    pass

# 9.3.1.179 Sensor Measurement Configuration
class IESensorMeasurementConfiguration(Packet):
    name="Sensor Measurement Configuration"
    fields_desc = []
    pass

# 9.3.1.180 Event Trigger Logged MDT Configuration
class IEEventTriggerLoggedMDTConfiguration(Packet):
    name="Event Trigger Logged MDT Configuration"
    fields_desc = []
    pass

# 9.3.1.181 NR Frequency Info
class IENRFrequencyInfo(Packet):
    name="NR Frequency Info"
    fields_desc = []
    pass

# 9.3.1.182 Area Scope of Neighbour Cells
class IEAreaScopeofNeighbourCells(Packet):
    name="Area Scope of Neighbour Cells"
    pass
    
# 9.3.1.183 NPN Paging Assistance Information
class IENPNPagingAssistanceInformation(Packet):
    name="NPN Paging Assistnace Information"
    fields_desc = []
    pass

# 9.3.1.184 NPN Mobility Information
class IENPNMobilityInformation(Packet):
    name="NPN Mobility Information"
    fields_desc = []
    pass

# 9.3.1.185 Cell CAG Information
class IECellCAGInformation(Packet):
    name="Cell CAG Information"
    fields_desc = []
    pass

# 9.3.1.186 Target to Source Failure Transparent Container
class IETargettoSourceFailureTransparentContainer(Packet):
    name="Target to Source Failure Transparent Container"
    fields_desc = []
    pass

# 9.3.1.187 Target NG-RAN Node to Source NG-RAN Node Failure Transparent Container
class IETargetNG_RANNodetoSourceNG_RANNodeFailureTransparentContainer(Packet):
    name="Target NG-RAN Node to Source NG-RAN Node Failure Transparent Container"
    pass

# 9.3.1.188 DAPS Request Information
class IEDAPSRequestInformation(Packet):
    name="DAPS Request Information"
    fields_desc = []
    pass

# 9.3.1.189 DAPS Response Information
class IEDAPSResponseInformation(Packet):
    name="DAPS Response Information"
    fields_desc = []
    pass

# 9.3.1.190 Early Status Transfer Transparent Container
class IEEarlyStatusTransferTransparentContainer(Packet):
    name="Early Status Transfer Transparent Container"
    fields_desc = []
    pass

# 9.3.1.191 Extended Slice Support List
class IEExtendedSliceSupportList(Packet):
    name="Extended Slice Support List"
    fields_desc = []
    pass

# 9.3.1.192 UE Capability Info Request
class IEUECapabilityInfoRequest(Packet):
    name="UE Capability Info Request"
    fields_desc = []
    pass

# 9.3.1.193 Extended RAN Node Name
class IEExtendedRANNodeName(Packet):
    name="Extended RAN Node Name"
    fields_desc = []
    pass

# 9.3.1.194 MICO All PLMN
class IEMICOAllPLMN(Packet):
    name="MICO All PLMN"
    fields_desc = []
    pass

# ----------------------------------------------------------------------------------------------------------
# 9.3.2 Transport Network Layer Related IEs
# 9.3.2.1 QoS Flow per TNL Information List
class IEQoSFlowperTNLInformationList(Packet):
    name="QoS Flow per TNL Information List"
    fields_desc = []
    pass

# 9.3.2.2 UP Transport Layer Information
class IEUPTransportLayerInformation(Packet):
    name="UP Transport Layer Information"
    fields_desc = []
    pass

# 9.3.2.3 E-RAB ID
class IEE_RABID(Packet):
    name="E-RAB ID"
    fields_desc = []
    pass

# 9.3.2.4 Transport Layer Address
class IETransportLayerAddress(Packet):
    name="Transport Layer Address"
    fields_desc = []
    pass

# 9.3.2.5 GTP-TEID
class IEGTP_TEID(Packet):
    name="GTP-TEID"
    fields_desc = []
    pass

# 9.3.2.6 CP Transport Layer Information
class IECPTransportLayerInformation(Packet):
    name="CP Transport Layer Information"
    fields_desc = []
    pass

# 9.3.2.7 TNL Association List
class IETNLAssociationList(Packet):
    name="TNL Association List"
    fields_desc = []
    pass

# 9.3.2.8 QoS Flow per TNL Information
class IEQoSFlowperTNLInformation(Packet):
    name="QoS Flow per TNL Information"
    fields_desc = []
    pass

# 9.3.2.9 TNL Association Usage
class IETNLAssociationUsage(Packet):
    name="TNL Association Usage"
    fields_desc = []
    pass

# 9.3.2.10 TNL Address Weight Factor
class IETNLAddressWeightFactor(Packet):
    name="TNL Address Weight Factor"
    fields_desc = []
    pass

# 9.3.2.11 UP Transport Layer Information Pair List
class IEUPTransportLayerInformationPairList(Packet):
    name="UP Transport Layer Information Pair List"
    pass

# 9.3.2.12 UP Transport Layer Information List
class IEUPTransportLayerInformationList(Packet):
    name="UP Transport Layer Information List"
    fields_desc = []
    pass

# 9.3.2.13 QoS Flow List with Data Forwarding
class IEQoSFlowListwithDataForwarding(Packet):
    name="QoS Flow List with Data Forwarding"
    fields_desc = []
    pass

# 9.3.2.14 URI
class IEURI(Packet):
    name="URI"
    fields_desc = []
    pass


# ----------------------------------------------------------------------------------------------------------
# 9.3.3 NAS Related IEs
# 9.3.3.1 AMF UE NGAP ID
class IEAMFUENGAPID(Packet):
    name="AMF UE NGAP ID"
    fields_desc = []
    pass

# 9.3.3.2 RAN UE NGAP ID
class IERANUENGAPID(Packet):
    name="RAN UE NGAP ID"
    fields_desc = []
    pass

# 9.3.3.3 GUAMI
class IEGUAMI(Packet):
    name="GUAMI"
    fields_desc = []
    pass

# 9.3.3.4 NAS-PDU
class IENAS_PDU(Packet):
    name="NAS-PDU"
    fields_desc = []
    pass

# 9.3.3.5 PLMN Identity
class IEPLMNIdentity(Packet):
    name="PLMN Identity"
    fields_desc = []
    pass

# 9.3.3.6 SON Configuration Transfer
class IESONConfigurationTransfer(Packet):
    name="SON Configuration Transfer"
    fields_desc = []
    pass

# 9.3.3.7 SON Information
class IESONInformation(Packet):
    name="SON Information"
    fields_desc = []
    pass

# 9.3.3.8 SON Information Reply
class IESONInformationReply(Packet):
    name="SON Information Reply"
    fields_desc = []
    pass

# 9.3.3.9 Xn TNL Configuration Info
class IEXnTNLConfigurationInfo(Packet):
    name="Xn TNL Configuration Info"
    fields_desc = []
    pass

# 9.3.3.10 TAC
class IETAC(Packet):
    name="TAC"
    fields_desc = []
    pass

# 9.3.3.11 TAI
class IETAI(Packet):
    name="TAI"
    fields_desc = []
    pass

# 9.3.3.12 AMF Set ID
class IEAMFSetID(Packet):
    name="AMF Set ID"
    fields_desc = []
    pass

# 9.3.3.13 Routing ID
class IERoutingID(Packet):
    name="Routing ID"
    fields_desc = []
    pass

# 9.3.3.14 NRPPa-PDU
class IENRPPa_PDU(Packet):
    name="NRPPa-PDU"
    fields_desc = []
    pass

# 9.3.3.15 RAN Paging Priority
class IERANPagingPriority(Packet):
    name="RAN Paging Priority"
    fields_desc = []
    pass

# 9.3.3.16 EPS TAC
class IEEPSTAC(Packet):
    name="EPS TAC"
    fields_desc = []
    pass

# 9.3.3.17 EPS TAI
class IEEPSTAI(Packet):
    name="EPS TAI"
    fields_desc = []
    pass

# 9.3.3.18 UE Paging Identity
class IEUEPagingIdentity(Packet):
    name="UE Paging Identity"
    fields_desc = []
    pass

# 9.3.3.19 AMF Pointer
class IEAMFPointer(Packet):
    name="AMF Pointer"
    fields_desc = []
    pass

# 9.3.3.20 5G-S-TMSI
class IE5G_S_TMSI(Packet):
    name="5G-S-TMSI"
    fields_desc = []
    pass

# 9.3.3.21 AMF Name
class IEAMFName(Packet):
    name="AMF Name"
    fields_desc = []
    pass

# 9.3.3.22 Paging Origin
class IEPagingOrigin(Packet):
    name="Paging Origin"
    fields_desc = []
    pass

# 9.3.3.23 UE Identity Index Value
class IEUEIdentityIndexValue(Packet):
    name="UE Identity Index Value"
    fields_desc = []
    pass

# 9.3.3.24 Periodic Registration Update Timer
class IEPeriodicRegistrationUpdateTimer(Packet):
    name="Periodic Registration Update Timer"
    fields_desc = []
    pass

# 9.3.3.25 UE-associated Logical NG-connection List
class IEUE_associatedLogicalNG_connectionList(Packet):
    name="UE-associated Logical NG-connection List"
    fields_desc = []
    pass

# 9.3.3.26 NAS Security Parameters from NG-RAN
class IENASSecurityParametersfromNG_RAN(Packet):
    name="NAS Security Parameters from NG-RAN"
    fields_desc = []
    pass

# 9.3.3.27 Source to Target AMF Information Reroute
class IESourcetoTargetAMFInformationReroute(Packet):
    name="Source to target AMF Information Reroute"
    fields_desc = []
    pass

# 9.3.3.28 RIM Information Transfer
class IERIMInformationTransfer(Packet):
    name="RIM Information Transfer"
    fields_desc = []
    pass

# 9.3.3.29 RIM Information
class IERIMInformation(Packet):
    name="RIM Information"
    fields_desc = []
    pass

# 9.3.3.30 LAI
class IELAI(Packet):
    name="LAI"
    fields_desc = []
    pass

# 9.3.3.31 Extended Connected Time
class IEExtendedConnectedTime(Packet):
    name="Extended Connected Time"
    fields_desc = []
    pass

# 9.3.3.32 End Indication
class IEEndIndication(Packet):
    name="End Indication"
    fields_desc = []
    pass

# 9.3.3.33 Inter-system SON Configuration Transfer
class IEInter_systemSONConfigurationTransfer(Packet):
    name="Inter-system SON Configuration Transfer"
    fields_desc = []
    pass

# 9.3.3.34 Inter-system SON Information
class IEInter_systemSONInformation(Packet):
    name="Inter-system SON Information"
    fields_desc = []
    pass

# 9.3.3.35 SON Information Report
class IESONInformationReport(Packet):
    name="SON Information Report"
    fields_desc = []
    pass

# 9.3.3.36 Inter-system SON Information Report
class IEInter_systemSONInformationReport(Packet):
    name="Inter-system SON Information Report"
    fields_desc = []
    pass

# 9.3.3.37 Failure Indication
class IEFailureIndication(Packet):
    name="Failure Indication"
    fields_desc = []
    pass

# 9.3.3.38 Inter-system Failure Indication
class IEIntersystemFailureIndication(Packet):
    name="Inter-system Failure Indication"
    fields_desc = []
    pass

# 9.3.3.39 HO Report
class IEHOReport(Packet):
    name="HO Report"
    fields_desc = []
    pass

# 9.3.3.40 Inter-system HO Report
class IEInter_systemHOReport(Packet):
    name="Inter-system HO Report"
    pass

# 9.3.3.41 UE RLF Report Container
class IEUERLFReportContainer(Packet):
    name="UE RLF Report Container"
    fields_desc = []
    pass

# 9.3.3.42 NID
class IENID(Packet):
    name="NID"
    fields_desc = []
    pass

# 9.3.3.43 CAG ID
class IECAGID(Packet):
    name="CAG ID"
    fields_desc = []
    pass

# 9.3.3.44 NPN Support
class IENPNSupport(Packet):
    name="NPN Support"
    fields_desc = []
    pass

# 9.3.3.45 Allowed PNI-NPN List
class IEAllowedPNI_NPNList(Packet):
    name="Allowed PNI-NPN List"
    fields_desc = []
    pass

# 9.3.3.46 NPN Access Information
class IENPNAccessInformation(Packet):
    name="NPN Access Information"
    fields_desc = []
    pass

# 9.3.3.47 Cell CAG List
class IECellCAGList(Packet):
    name="Cell CAG List"
    fields_desc = []
    pass

# 9.3.3.48 UL CP Security Information
class IEULCPSecurityInformation(Packet):
    name="UL CP Security Information"
    fields_desc = []
    pass

# 9.3.3.49 DL CP Security Information
class IEDLCPSecurityInformation(Packet):
    name="DL CP Security Information"
    fields_desc = []
    pass

# 9.3.3.50 Configured TAC Indication
class IEConfiguredTACIndication(Packet):
    name="Configured TAC Indication"
    fields_desc = []
    pass

# 9.3.3.51 Extended AMF Name
class IEExtendedAMFName(Packet):
    name="Extended AMF Name"
    fields_desc = []
    pass

# 9.3.3.52 Extended UE Identity Index Value
class IEExtendedUEIdentityIndexValue(Packet):
    name="Extended UE Identity Index Value"
    fields_desc = []
    pass


# ----------------------------------------------------------------------------------------------------------
# 9.3.4 SMF Related IEs

# 9.3.4.1 PDU Session Resource Setup Request Transfer
class IEPDUSessionResourceSetupRequestTransfer(Packet):
    name="PDU Session Resource Setup Request Transfer"
    fields_desc = []
    pass

# 9.3.4.2 PDU Session Resource Setup Response Transfer
class IEPDUSessionResourceSetupResponseTransfer(Packet):
    name="PDU Session Resource Setup Response Transfer"
    fields_desc = []
    pass

# 9.3.4.3 PDU Session Resource Modify Request Transfer
class IEPDUSessionResourceModifyRequestTransfer(Packet):
    name="PDU Session Resource Modify Request Transfer"
    fields_desc = []
    pass

# 9.3.4.4 PDU Session Resource Modify Response Transfer
class IEPDUSessionResourceModifyResponseTransfer(Packet):
    name="PDU Session Reource Modify Response Transfer"
    fields_desc = []
    pass

# 9.3.4.5 PDU Session Resource Notify Transfer
class IEPDUSessionResourceNotifyTransfer(Packet):
    name="PDU Session Resource Notify Transfer"
    fields_desc = []
    pass

# 9.3.4.6 PDU Session Resource Modify Indication Transfer
class IEPDUSessionResourceModifyIndicationTransfer(Packet):
    name="PDU Session Resource Modify Indication Transfer"
    fields_desc = []
    pass

# 9.3.4.7 PDU Session Resource Modify Confirm Transfer
class IEPDUSessionResourceModifyConfirmTransfer(Packet):
    name="PDU Session Resource Modify Confirm Transfer"
    fields_desc = []
    pass

# 9.3.4.8 Path Switch Request Transfer
class IEPathSwitchRequestTransfer(Packet):
    name="Path Switch Request Transfer"
    fields_desc = []
    pass

# 9.3.4.9 Path Switch Request Acknowledge Transfer
class IEPathSwitchRequestAcknowledgeTransfer(Packet):
    name="Path Switch Request Acknowledge Transfer"
    fields_desc = []
    pass

# 9.3.4.10 Handover Command Transfer
class IEHandoverCommandTransfer(Packet):
    name="Handover Command Transfer"
    fields_desc = []
    pass

# 9.3.4.11 Handover Request Acknowledge Transfer
class IEHandoverRequestAcknowledgeTransfer(Packet):
    name="Handover Request Acknowledge Transfer"
    fields_desc = []
    pass

# 9.3.4.12 PDU Session Resource Release Command Transfer
class IEPDUSessionResourceReleaseCommandTransfer(Packet):
    name="PDU Session Resource Release Command Transfer"
    fields_desc = []
    pass

# 9.3.4.13 PDU Session Resource Notify Released Transfer
class IEPDUSessionResourceNotifyReleasedTransfer(Packet):
    name="PDU Session Resource Notify Released Transfer"
    fields_desc = []
    pass

# 9.3.4.14 Handover Required Transfer
class IEHandoverRequiredTransfer(Packet):
    name="Handover Required Transfer"
    fields_desc = []
    pass

# 9.3.4.15 Path Switch Request Setup Failed Transfer
class IEPathSwitchRequestSetupFailedTransfer(Packet):
    name="Path Switch Request Setup Failed Transfer"
    fields_desc = []
    pass

# 9.3.4.16 PDU Session Resource Setup Unsuccessful Transfer
class IEPDUSessionResourceSetupUnsuccessfulTransfer(Packet):
    name="PDU Session Resource Setup Unsuccessful Transfer"
    fields_desc = []
    pass

# 9.3.4.17 PDU Session Resource Modify Unsuccessful Transfer
class IEPDUSessionResourceModifyUnsuccessfulTransfer(Packet):
    name="PDU Session Resource Modify Unsuccessful Transfer"
    fields_desc = []
    pass

# 9.3.4.18 Handover Preparation Unsuccessful Transfer
class IEHandoverPreparationUnsuccessfulTransfer(Packet):
    name="Handover Preparation unsuccessful Transfer"
    fields_desc = []
    pass

# 9.3.4.19 Handover Resource Allocation Unsuccessful Transfer
class IEHandoverResourceAllocationUnsuccessfulTransfer(Packet):
    name="Handover Resource Allocation Unsuccessful Transfer"
    fields_desc = []
    pass

# 9.3.4.20 Path Switch Request Unsuccessful Transfer
class IEPathSwitchRequestUnsuccessfulTransfer(Packet):
    name="Path Switch Request Unsuccessful Transfer"
    fields_desc = []
    pass

# 9.3.4.21 PDU Session Resource Release Response Transfer
class IEPDUSessionResourceReleaseResponseTransfer(Packet):
    name="PDU Session Resource Release Response Transfer"
    fields_desc = []
    pass

# 9.3.4.22 PDU Session Resource Modify Indication Unsuccessful Transfer
class IEPDUSessionResourceModifyIndicationUnsuccessfulTransfer(Packet):
    name="PDU Session Resource Modify Indication Unsuccessful Transfer"
    fields_desc = []
    pass

# 9.3.4.23 Secondary RAT Data Usage Report Transfer
class IESecondaryRATDataUsageReportTransfer(Packet):
    name="Secondary RAT Data Usage Report Transfer"
    fields_desc = []
    pass

# 9.3.4.24 UE Context Resume Request Transfer
class IEUEContextResumeRequestTransfer(Packet):
    name="UE Context Resume Request Transfer"
    fields_desc = []
    pass

# 9.3.4.25 UE Context Resume Response Transfer
class IEUEContextResumeResponseTransfer(Packet):
    name="UE Context Resume Response Transfer"
    fields_desc = []
    pass

# 9.3.4.26 UE Context Suspend Request Transfer
class IEUEContextSuspendRequestTransfer(Packet):
    name="UE Context Suspend Request Transfer"
    pass


