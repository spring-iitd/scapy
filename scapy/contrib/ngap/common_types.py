# SPDX-License-Identifier: GPL-2.0-only
# This file is part of Scapy
# See https://scapy.net/ for more information
# Copyright (C) 2018 Mayank Singh Kushwaha <mayanksinghk8@gmail.com>

# scapy.contrib.description = NG Application Protocol (NGAP)
# scapy.contrib.status = skip

"""
NG Application Protocol (NGAP)

Spec: 3GPP TS 38.413
"""

import struct

from scapy.compat import chb, orb, bytes_encode
from scapy.config import conf
from scapy.error import warning
from scapy.fields import (
    BitEnumField,
    BitField,
    ByteEnumField,
    ByteField,
    ConditionalField,
    FieldLenField,
    FieldListField,
    FlagsField,
    IPField,
    IntField,
    PacketListField,
    ShortField,
    StrFixedLenField,
    StrLenField,
    X3BytesField,
    XBitField,
    XByteField,
    XIntField,
)
from scapy.layers.inet import IP, UDP
from scapy.layers.inet6 import IPv6, IP6Field
from scapy.layers.ppp import PPP
from scapy.packet import bind_layers, bind_bottom_up, bind_top_down, \
    Packet, Raw
from scapy.volatile import RandInt, RandIP, RandNum, RandString


ElementaryProcedures = {
    0: "id-AMFConfigurationUpdate",
    1: "id-AMFStatusIndication",
    2: "id-CellTrafficTrace",
    3: "id-DeactivateTrace",
    4: "id-DownlinkNASTransport",
    5: "id-DownlinkNonUEAssociatedNRPPaTransport",
    6: "id- DownlinkRANConfigurationTransfer",
    7: "id-DownlinkRANStatusTransfer",
    8: "id-DownlinkUEAssociatedNRPPaTransport",
    9: "id-ErrorIndication",
    10: "id-HandoverCancel",
    11: "id-HandoverNotification",
    12: "id-HandoverPreparation",
    13: "id-HandoverResourceAllocation",
    14: "id-InitialContextSetup",
    15: "id-InitialUEMessage",
    16: "id-LocationReportingControl",
    17: "id-LocationReportingFailureIndication",
    18: "id-LocationReport",
    19: "id-NASNonDeliveryIndication",
    20: "id-NGReset",
    21: "id-NGSetup",
    22: "id-OverloadStart",
    23: "id-OverloadStop",
    24: "id-Paging",
    25: "id-PathSwitchRequest",
    26: "id-PDUSessionResourceModify",
    27: "id-PDUSessionResourceModifyIndication",
    28: "id-PDUSessionResourceRelease",
    29: "id-PDUSessionResourceSetup",
    30: "id-PDUSessionResourceNotify",
    31: "id-PrivateMessage",
    32: "id-PWSCancel",
    33: "id-PWSFailureIndication",
    34: "id-PWSRestartIndication",
    35: "id-RANConfigurationUpdate",
    36: "id-RerouteNASRequest",
    37: "id-RRCInactiveTransitionReport",
    38: "id-TraceFailureIndication",
    39: "id-TraceStart",
    40: "id-UEContextModification",
    41: "id-UEContextRelease",
    42: "id-UEContextReleaseRequest",
    43: "id-UERadioCapabilityCheck",
    44: "id-UERadioCapabilityInfoIndication",
    45: "id-UETNLABindingRelease",
    46: "id-UplinkNASTransport",
    47: "id-UplinkNonUEAssociatedNRPPaTransport",
    48: "id-UplinkRANConfigurationTransfer",
    49: "id-UplinkRANStatusTransfer",
    50: "id-UplinkUEAssociatedNRPPaTransport",
    51: "id-WriteReplaceWarning",
    52: "id-SecondaryRATDataUsageReport",
    53: "id-UplinkRIMInformationTransfer",
    54: "id-DownlinkRIMInformationTransfer",
    55: "id-RetrieveUEInformation",
    56: "id-UEInformationTransfer",
    57: "id-RANCPRelocationIndication",
    58: "id-UEContextResume",
    59: "id-UEContextSuspend",
    60: "id-UERadioCapabilityIDMapping",
    61: "id-HandoverSuccess",
    62: "id-UplinkRANEarlyStatusTransfer",
    63: "id-DownlinkRANEarlyStatusTransfer",
    64: "id-AMFCPRelocationIndication",
    65: "id-ConnectionEstablishmentIndication"
}

# Extension Constants
maxPrivateIEs = 65535
maxProtocolExtension = 65535
maxProtocolIEs = 65535

# Lists
maxnoofAllowedAreas = 16
maxnoofAllowedCAGsperPLMN = 256
maxnoofAllowedS_NSSAIs = 8
maxnoofBluetoothName = 4
maxnoofBPLMNs = 12
maxnoofCAGSperCell = 64
maxnoofCellIDforMDT = 32
maxnoofCellIDforWarning = 65535
maxnoofCellinAoI = 256
maxnoofCellinEAI = 65535
maxnoofCellinTAI = 65535
maxnoofCellsingNB = 16384
maxnoofCellsinngeNB = 256
maxnoofCellsinUEHistoryInfo = 16
maxnoofCellsUEMovingTrajectory = 16
maxnoofDRBs = 32
maxnoofEmergencyAreaID = 65535
maxnoofEAIforRestart = 256
maxnoofEPLMNs = 15
maxnoofEPLMNsPlusOne = 16
maxnoofE_RABs = 256
maxnoofErrors = 256
maxnoofExtSliceItems = 65535
maxnoofForbTACs = 4096
maxnoofFreqforMDT = 8
maxnoofMDTPLMNs = 16
maxnoofMultiConnectivity = 4
maxnoofMultiConnectivityMinusOne = 3
maxnoofNeighPCIforMDT = 32
maxnoofNGConnectionsToReset = 65536
maxnoofNRCellBands = 32
maxnoofPC5QoSFlows = 2048
maxnoofPDUSessions = 256
maxnoofPLMNs = 12
maxnoofQosFlows = 64
maxnoofQosParaSets = 8
maxnoofRANNodeinAoI = 64
maxnoofRecommendedCells = 16
maxnoofRecommendedRANNodes = 16
maxnoofAoI = 64
maxnoofSensorName = 3
maxnoofServedGUAMIs = 256
maxnoofSliceItems = 1024
maxnoofTACs = 256
maxnoofTAforMDT = 8
maxnoofTAIforInactive = 16
maxnoofTAIforPaging = 16
maxnoofTAIforRestart = 2048
maxnoofTAIforWarning = 65535
maxnoofTAIinAoI = 16
maxnoofTimePeriods = 2
maxnoofTNLAssociations = 32
maxnoofWLANName = 4
maxnoofXnExtTLAs = 16
maxnoofXnGTP_TLAs = 16
maxnoofXnTLAs = 2
maxnoofCandidateCells = 32
maxNRARFCN = 3279165

# Information Element
IEs = {
    0: "id-AllowedNSSAI",
    1: "id-AMFName",
    2: "id-AMFOverloadResponse",
    3: "id-AMFSetID",
    4: "id-AMF-TNLAssociationFailedToSetupList",
    5: "id-AMF-TNLAssociationSetupList",
    6: "id-AMF-TNLAssociationToAddList",
    7: "id-AMF-TNLAssociationToRemoveList",
    8: "id-AMF-TNLAssociationToUpdateList",
    9: "id-AMFTrafficLoadReductionIndication",
    10: "id-AMF-UE-NGAP-ID",
    11: "id-AssistanceDataForPaging",
    12: "id-BroadcastCancelledAreaList",
    13: "id-BroadcastCompletedAreaList",
    14: "id-CancelAllWarningMessages",
    15: "id-Cause",
    16: "id-CellIDListForRestart",
    17: "id-ConcurrentWarningMessageInd",
    18: "id-CoreNetworkAssistanceInformationForInactive",
    19: "id-CriticalityDiagnostics",
    20: "id-DataCodingScheme",
    21: "id-DefaultPagingDRX",
    22: "id-DirectForwardingPathAvailability",
    23: "id-EmergencyAreaIDListForRestart",
    24: "id-EmergencyFallbackIndicator",
    25: "id-EUTRA-CGI",
    26: "id-FiveG-S-TMSI",
    27: "id-GlobalRANNodeID",
    28: "id-GUAMI",
    29: "id-HandoverType",
    30: "id-IMSVoiceSupportIndicator",
    31: "id-IndexToRFSP",
    32: "id-InfoOnRecommendedCellsAndRANNodesForPaging",
    33: "id-LocationReportingRequestType",
    34: "id-MaskedIMEISV",
    35: "id-MessageIdentifier",
    36: "id-MobilityRestrictionList",
    37: "id-NASC",
    38: "id-NAS-PDU",
    39: "id-NASSecurityParametersFromNGRAN",
    40: "id-NewAMF-UE-NGAP-ID",
    41: "id-NewSecurityContextInd",
    42: "id-NGAP-Message",
    43: "id-NGRAN-CGI",
    44: "id-NGRANTraceID",
    45: "id-NR-CGI",
    46: "id-NRPPa-PDU",
    47: "id-NumberOfBroadcastsRequested",
    48: "id-OldAMF",
    49: "id-OverloadStartNSSAIList",
    50: "id-PagingDRX",
    51: "id-PagingOrigin",
    52: "id-PagingPriority",
    53: "id-PDUSessionResourceAdmittedList",
    54: "id-PDUSessionResourceFailedToModifyListModRes",
    55: "id-PDUSessionResourceFailedToSetupListCxtRes",
    56: "id-PDUSessionResourceFailedToSetupListHOAck",
    57: "id-PDUSessionResourceFailedToSetupListPSReq",
    58: "id-PDUSessionResourceFailedToSetupListSURes",
    59: "id-PDUSessionResourceHandoverList",
    60: "id-PDUSessionResourceListCxtRelCpl",
    61: "id-PDUSessionResourceListHORqd",
    62: "id-PDUSessionResourceModifyListModCfm",
    63: "id-PDUSessionResourceModifyListModInd",
    64: "id-PDUSessionResourceModifyListModReq",
    65: "id-PDUSessionResourceModifyListModRes",
    66: "id-PDUSessionResourceNotifyList",
    67: "id-PDUSessionResourceReleasedListNot",
    68: "id-PDUSessionResourceReleasedListPSAck",
    69: "id-PDUSessionResourceReleasedListPSFail",
    70: "id-PDUSessionResourceReleasedListRelRes",
    71: "id-PDUSessionResourceSetupListCxtReq",
    72: "id-PDUSessionResourceSetupListCxtRes",
    73: "id-PDUSessionResourceSetupListHOReq",
    74: "id-PDUSessionResourceSetupListSUReq",
    75: "id-PDUSessionResourceSetupListSURes",
    76: "id-PDUSessionResourceToBeSwitchedDLList",
    77: "id-PDUSessionResourceSwitchedList",
    78: "id-PDUSessionResourceToReleaseListHOCmd",
    79: "id-PDUSessionResourceToReleaseListRelCmd",
    80: "id-PLMNSupportList",
    81: "id-PWSFailedCellIDList",
    82: "id-RANNodeName",
    83: "id-RANPagingPriority",
    84: "id-RANStatusTransfer-TransparentContainer",
    85: "id-RAN-UE-NGAP-ID",
    86: "id-RelativeAMFCapacity",
    87: "id-RepetitionPeriod",
    88: "id-ResetType",
    89: "id-RoutingID",
    90: "id-RRCEstablishmentCause",
    91: "id-RRCInactiveTransitionReportRequest",
    92: "id-RRCState",
    93: "id-SecurityContext",
    94: "id-SecurityKey",
    95: "id-SerialNumber",
    96: "id-ServedGUAMIList",
    97: "id-SliceSupportList",
    98: "id-SONConfigurationTransferDL",
    99: "id-SONConfigurationTransferUL",
    100: "id-SourceAMF-UE-NGAP-ID",
    101: "id-SourceToTarget-TransparentContainer",
    102: "id-SupportedTAList",
    103: "id-TAIListForPaging",
    104: "id-TAIListForRestart",
    105: "id-TargetID",
    106: "id-TargetToSource-TransparentContainer",
    107: "id-TimeToWait",
    108: "id-TraceActivation",
    109: "id-TraceCollectionEntityIPAddress",
    110: "id-UEAggregateMaximumBitRate",
    111: "id-UE-associatedLogicalNG-connectionList",
    112: "id-UEContextRequest",
    114: "id-UE-NGAP-IDs",
    115: "id-UEPagingIdentity",
    116: "id-UEPresenceInAreaOfInterestList",
    117: "id-UERadioCapability",
    118: "id-UERadioCapabilityForPaging",
    119: "id-UESecurityCapabilities",
    120: "id-UnavailableGUAMIList",
    121: "id-UserLocationInformation",
    122: "id-WarningAreaList",
    123: "id-WarningMessageContents",
    124: "id-WarningSecurityInfo",
    125: "id-WarningType",
    126: "id-AdditionalUL-NGU-UP-TNLInformation",
    127: "id-DataForwardingNotPossible",
    128: "id-DL-NGU-UP-TNLInformation",
    129: "id-NetworkInstance",
    130: "id-PDUSessionAggregateMaximumBitRate",
    131: "id-PDUSessionResourceFailedToModifyListModCfm",
    132: "id-PDUSessionResourceFailedToSetupListCxtFail",
    133: "id-PDUSessionResourceListCxtRelReq",
    134: "id-PDUSessionType",
    135: "id-QosFlowAddOrModifyRequestList",
    136: "id-QosFlowSetupRequestList",
    137: "id-QosFlowToReleaseList",
    138: "id-SecurityIndication",
    139: "id-UL-NGU-UP-TNLInformation",
    140: "id-UL-NGU-UP-TNLModifyList",
    141: "id-WarningAreaCoordinates",
    142: "id-PDUSessionResourceSecondaryRATUsageList",
    143: "id-HandoverFlag",
    144: "id-SecondaryRATUsageInformation",
    145: "id-PDUSessionResourceReleaseResponseTransfer",
    146: "id-RedirectionVoiceFallback",
    147: "id-UERetentionInformation",
    148: "id-S-NSSAI",
    149: "id-PSCellInformation",
    150: "id-LastEUTRAN-PLMNIdentity",
    151: "id-MaximumIntegrityProtectedDataRate-DL",
    152: "id-AdditionalDLForwardingUPTNLInformation",
    153: "id-AdditionalDLUPTNLInformationForHOList",
    154: "id-AdditionalNGU-UP-TNLInformation",
    155: "id-AdditionalDLQosFlowPerTNLInformation",
    156: "id-SecurityResult",
    157: "id-ENDC-SONConfigurationTransferDL",
    158: "id-ENDC-SONConfigurationTransferUL",
    159: "id-OldAssociatedQosFlowList-ULendmarkerexpected",
    160: "id-CNTypeRestrictionsForEquivalent",
    161: "id-CNTypeRestrictionsForServing",
    162: "id-NewGUAMI",
    163: "id-ULForwarding",
    164: "id-ULForwardingUP-TNLInformation",
    165: "id-CNAssistedRANTuning",
    166: "id-CommonNetworkInstance",
    167: "id-NGRAN-TNLAssociationToRemoveList",
    168: "id-TNLAssociationTransportLayerAddressNGRAN",
    169: "id-EndpointIPAddressAndPort",
    170: "id-LocationReportingAdditionalInfo",
    171: "id-SourceToTarget-AMFInformationReroute",
    172: "id-AdditionalULForwardingUPTNLInformation",
    173: "id-SCTP-TLAs",
    174: "id-SelectedPLMNIdentity",
    175: "id-RIMInformationTransfer",
    176: "id-GUAMIType",
    177: "id-SRVCCOperationPossible",
    178: "id-TargetRNC-ID",
    179: "id-RAT-Information",
    180: "id-ExtendedRATRestrictionInformation",
    181: "id-QosMonitoringRequest",
    182: "id-SgNB-UE-X2AP-ID",
    183: "id-AdditionalRedundantDL-NGU-UP-TNLInformation",
    184: "id-AdditionalRedundantDLQosFlowPerTNLInformation",
    185: "id-AdditionalRedundantNGU-UP-TNLInformation",
    186: "id-AdditionalRedundantUL-NGU-UP-TNLInformation",
    187: "id-CNPacketDelayBudgetDL",
    188: "id-CNPacketDelayBudgetUL",
    189: "id-ExtendedPacketDelayBudget",
    190: "id-RedundantCommonNetworkInstance",
    191: "id-RedundantDL-NGU-TNLInformationReused",
    192: "id-RedundantDL-NGU-UP-TNLInformation",
    193: "id-RedundantDLQosFlowPerTNLInformation",
    194: "id-RedundantQosFlowIndicator",
    195: "id-RedundantUL-NGU-UP-TNLInformation",
    196: "id-TSCTrafficCharacteristics",
    197: "id-RedundantPDUSessionInformation",
    198: "id-UsedRSNInformation",
    199: "id-IAB-Authorized",
    200: "id-IAB-Supported",
    201: "id-IABNodeIndication",
    202: "id-NB-IoT-PagingDRX",
    203: "id-NB-IoT-Paging-eDRXInfo",
    204: "id-NB-IoT-DefaultPagingDRX",
    205: "id-Enhanced-CoverageRestriction",
    206: "id-Extended-ConnectedTime",
    207: "id-PagingAssisDataforCEcapabUE",
    208: "id-WUS-Assistance-Information",
    209: "id-UE-DifferentiationInfo",
    210: "id-NB-IoT-UEPriority",
    211: "id-UL-CP-SecurityInformation",
    212: "id-DL-CP-SecurityInformation",
    213: "id-TAI",
    214: "id-UERadioCapabilityForPagingOfNB-IoT",
    215: "id-LTEV2XServicesAuthorized",
    216: "id-NRV2XServicesAuthorized",
    217: "id-LTEUESidelinkAggregateMaximumBitrate",
    218: "id-NRUESidelinkAggregateMaximumBitrate",
    219: "id-PC5QoSParameters",
    220: "id-AlternativeQoSParaSetList",
    221: "id-CurrentQoSParaSetIndex",
    222: "id-CEmodeBrestricted",
    223: "id-PagingeDRXInformation",
    224: "id-CEmodeBSupport-Indicator",
    225: "id-LTEM-Indication",
    226: "id-EndIndication",
    227: "id-EDT-Session",
    228: "id-UECapabilityInfoRequest",
    229: "id-PDUSessionResourceFailedToResumeListRESReq",
    230: "id-PDUSessionResourceFailedToResumeListRESRes",
    231: "id-PDUSessionResourceSuspendListSUSReq",
    232: "id-PDUSessionResourceResumeListRESReq",
    233: "id-PDUSessionResourceResumeListRESRes",
    234: "id-UE-UP-CIoT-Support",
    235: "id-Suspend-Request-Indication",
    236: "id-Suspend-Response-Indication",
    237: "id-RRC-Resume-Cause",
    238: "id-RGLevelWirelineAccessCharacteristics",
    239: "id-W-AGFIdentityInformation",
    240: "id-GlobalTNGF-ID",
    241: "id-GlobalTWIF-ID",
    242: "id-GlobalW-AGF-ID",
    243: "id-UserLocationInformationW-AGF",
    244: "id-UserLocationInformationTNGF",
    245: "id-AuthenticatedIndication",
    246: "id-TNGFIdentityInformation",
    247: "id-TWIFIdentityInformation",
    248: "id-UserLocationInformationTWIF",
    249: "id-DataForwardingResponseERABList",
    250: "id-IntersystemSONConfigurationTransferDL",
    251: "id-IntersystemSONConfigurationTransferUL",
    252: "id-SONInformationReport",
    253: "id-UEHistoryInformationFromTheUE",
    254: "id-ManagementBasedMDTPLMNList",
    255: "id-MDTConfiguration",
    256: "id-PrivacyIndicator",
    257: "id-TraceCollectionEntityURI",
    258: "id-NPN-Support",
    259: "id-NPN-AccessInformation",
    260: "id-NPN-PagingAssistanceInformation",
    261: "id-NPN-MobilityInformation",
    262: "id-TargettoSource-Failure-TransparentContainer",
    263: "id-NID",
    264: "id-UERadioCapabilityID",
    265: "id-UERadioCapability-EUTRA-Format",
    266: "id-DAPSRequestInfo",
    267: "id-DAPSResponseInfoList",
    268: "id-EarlyStatusTransfer-TransparentContainer",
    269: "id-NotifySourceNGRANNode",
    270: "id-ExtendedSliceSupportList",
    271: "id-ExtendedTAISliceSupportList",
    272: "id-ConfiguredTACIndication",
    273: "id-Extended-RANNodeName",
    274: "id-Extended-AMFName",
    275: "id-GlobalCable-ID",
    276: "id-QosMonitoringReportingFrequency",
    277: "id-QosFlowParametersList",
    278: "id-QosFlowFeedbackList",
    279: "id-BurstArrivalTimeDownlink",
    280: "id-ExtendedUEIdentityIndexValue",
    281: "id-PduSessionExpectedUEActivityBehaviour",
    282: "id-MicoAllPLMN",
    283: "id-QosFlowFailedToSetupList"
}

# Criticality
Criticality = {
    0 : "reject",
    1 : "ignore",
    2 : "notify"
}


TriggeringMessage = {
    0 : "initiating-message",
    1 : "successful-outcome",
    2 : "unsuccessful-outcome"
}