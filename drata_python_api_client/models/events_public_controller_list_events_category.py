from enum import Enum


class EventsPublicControllerListEventsCategory(str, Enum):
    ACCESS_REVIEW = "ACCESS_REVIEW"
    AGENT = "AGENT"
    ASSESSMENT = "ASSESSMENT"
    ASSET = "ASSET"
    AUDIT = "AUDIT"
    AUTOPILOT = "AUTOPILOT"
    AUTOPILOT_RECIPE = "AUTOPILOT_RECIPE"
    AUTOPILOT_RECIPE_SCHEDULE = "AUTOPILOT_RECIPE_SCHEDULE"
    CLOUD_STORAGE = "CLOUD_STORAGE"
    CODEBASE = "CODEBASE"
    COMPANY = "COMPANY"
    COMPANY_NOTIFICATION = "COMPANY_NOTIFICATION"
    CONNECTION = "CONNECTION"
    CUSTOM_CONNECTION = "CUSTOM_CONNECTION"
    CUSTOM_FRAMEWORKS = "CUSTOM_FRAMEWORKS"
    DEVICE = "DEVICE"
    DOCUMENT_SCANNED = "DOCUMENT_SCANNED"
    EVIDENCE = "EVIDENCE"
    EXCEPTION_MANAGEMENT = "EXCEPTION_MANAGEMENT"
    GRC = "GRC"
    MDM = "MDM"
    MONITOR = "MONITOR"
    MULTIPLE_PRODUCT_SUPPORT = "MULTIPLE_PRODUCT_SUPPORT"
    PERSONNEL = "PERSONNEL"
    POLICY = "POLICY"
    PUBLIC_API_KEY = "PUBLIC_API_KEY"
    QUESTIONNAIRE = "QUESTIONNAIRE"
    REPORT = "REPORT"
    RESYNC = "RESYNC"
    RISK = "RISK"
    SERVICE_PROVIDER = "SERVICE_PROVIDER"
    TASK = "TASK"
    TRUST_CENTER_PRIVATE_ACCESS = "TRUST_CENTER_PRIVATE_ACCESS"
    TRUST_CENTER_REPORTS = "TRUST_CENTER_REPORTS"
    TRUST_PAGES = "TRUST_PAGES"
    USER = "USER"
    VENDOR = "VENDOR"
    VENDOR_PROFILE = "VENDOR_PROFILE"
    WORKFLOWS = "WORKFLOWS"

    def __str__(self) -> str:
        return str(self.value)
