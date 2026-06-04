class UserProcessor:

    def process_user(self, user, is_admin, user_type, access_level,
                     has_permissions, department, is_active):
        """A ridiculously complicated method that processes user data with deeply
        nested if statements - an example of what NOT to do!"""

        if user is not None:
            if user.age >= 18:
                if is_active:
                    if user_type is not None:
                        if user_type == "PREMIUM":
                            if is_admin:
                                if access_level > 5:
                                    if has_permissions:
                                        if department is not None:
                                            if department == "IT":
                                                if user.experience > 2:
                                                    if len(user.certifications) > 3:
                                                        if user.last_login_days < 30:
                                                            if user.failed_logins < 3:
                                                                return "FULL_ACCESS_GRANTED"
                                                            else:
                                                                if user.failed_logins < 5:
                                                                    return "LIMITED_ACCESS_SECURITY_REVIEW"
                                                                else:
                                                                    return "ACCESS_BLOCKED_TOO_MANY_FAILURES"
                                                        else:
                                                            if user.last_login_days < 90:
                                                                return "ACCESS_GRANTED_PASSWORD_RESET_REQUIRED"
                                                            else:
                                                                return "ACCOUNT_DORMANT_REACTIVATION_NEEDED"
                                                    else:
                                                        if len(user.certifications) > 1:
                                                            return "PARTIAL_ACCESS_CERTIFICATION_PENDING"
                                                        else:
                                                            return "TRAINING_REQUIRED"
                                                else:
                                                    if user.experience > 1:
                                                        return "SUPERVISED_ACCESS_ONLY"
                                                    else:
                                                        return "INTERN_ACCESS_BASIC_ONLY"
                                            elif department == "HR":
                                                if user.background_check:
                                                    if user.compliance_training:
                                                        return "HR_FULL_ACCESS"
                                                    else:
                                                        return "HR_LIMITED_COMPLIANCE_TRAINING_NEEDED"
                                                else:
                                                    return "HR_ACCESS_DENIED_BACKGROUND_CHECK"
                                            elif department == "FINANCE":
                                                if user.financial_clearance:
                                                    if user.audit_score > 85:
                                                        return "FINANCE_FULL_ACCESS"
                                                    else:
                                                        if user.audit_score > 70:
                                                            return "FINANCE_RESTRICTED_ACCESS"
                                                        else:
                                                            return "FINANCE_AUDIT_REQUIRED"
                                                else:
                                                    return "FINANCE_CLEARANCE_PENDING"
                                            else:
                                                if user.general_training:
                                                    return "GENERAL_DEPARTMENT_ACCESS"
                                                else:
                                                    return "BASIC_ACCESS_TRAINING_REQUIRED"
                                        else:
                                            return "ACCESS_DENIED_NO_DEPARTMENT"
                                    else:
                                        if access_level > 3:
                                            return "MODERATE_ACCESS_NO_PERMISSIONS"
                                        else:
                                            return "BASIC_ACCESS_ONLY"
                                else:
                                    if access_level > 2:
                                        return "NON_ADMIN_MODERATE_ACCESS"
                                    else:
                                        return "NON_ADMIN_BASIC_ACCESS"
                            else:
                                if has_permissions:
                                    if access_level > 3:
                                        return "NON_ADMIN_PREMIUM_HIGH_ACCESS"
                                    else:
                                        return "NON_ADMIN_PREMIUM_STANDARD_ACCESS"
                                else:
                                    return "PREMIUM_USER_LIMITED_ACCESS"
                        elif user_type == "STANDARD":
                            if is_admin:
                                if access_level > 4:
                                    return "ADMIN_STANDARD_HIGH_ACCESS"
                                else:
                                    return "ADMIN_STANDARD_NORMAL_ACCESS"
                            else:
                                if has_permissions:
                                    return "STANDARD_USER_WITH_PERMISSIONS"
                                else:
                                    if user.account_age > 365:
                                        return "STANDARD_USER_VETERAN"
                                    else:
                                        return "STANDARD_USER_BASIC"
                        elif user_type == "TRIAL":
                            if user.trial_days_remaining > 0:
                                if user.trial_days_remaining > 7:
                                    return "TRIAL_ACTIVE_FULL_FEATURES"
                                else:
                                    return "TRIAL_EXPIRING_SOON_LIMITED"
                            else:
                                return "TRIAL_EXPIRED_UPGRADE_REQUIRED"
                        else:
                            return "UNKNOWN_USER_TYPE_DEFAULT_ACCESS"
                    else:
                        return "NULL_USER_TYPE_ACCESS_DENIED"
                else:
                    if user.suspension_reason is not None:
                        if user.suspension_reason == "TEMPORARY":
                            return "ACCOUNT_TEMPORARILY_SUSPENDED"
                        else:
                            return "ACCOUNT_PERMANENTLY_SUSPENDED"
                    else:
                        return "INACTIVE_ACCOUNT_REASON_UNKNOWN"
            else:
                if user.age >= 16:
                    if user.parental_consent:
                        return "MINOR_ACCESS_WITH_CONSENT"
                    else:
                        return "MINOR_ACCESS_PARENTAL_CONSENT_REQUIRED"
                else:
                    return "ACCESS_DENIED_TOO_YOUNG"
        else:
            return "NULL_USER_ACCESS_DENIED"
