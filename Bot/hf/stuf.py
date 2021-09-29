def get_tle_mof_t(recvd_text: str) -> (str, str):
    try:
        cmnd_message, reason = recvd_text.split(" ", 1)
    except ValueError:
        cmnd_message, reason = recvd_text, ""
    cmnd_message = cmnd_message.strip()
    reason = reason.strip()
    return cmnd_message, reason
