from mopidy_mpd import exceptions, protocol


@protocol.commands.add("disableoutput", outputid=protocol.UINT)
def disableoutput(context, outputid):
    """
    *musicpd.org, audio output section:*

        ``disableoutput {ID}``

        Turns an output off.
    """
    if outputid == 0:
        success = context.core.mixer.set_mute(False).get()
        if not success:
            raise exceptions.MpdSystemError("problems disabling output")
    else:
        raise exceptions.MpdNoExistError("No such audio output")


@protocol.commands.add("enableoutput", outputid=protocol.UINT)
def enableoutput(context, outputid):
    """
    *musicpd.org, audio output section:*

        ``enableoutput {ID}``

        Turns an output on.
    """
    if outputid == 0:
        success = context.core.mixer.set_mute(True).get()
        if not success:
            raise exceptions.MpdSystemError("problems enabling output")
    else:
        raise exceptions.MpdNoExistError("No such audio output")


@protocol.commands.add("toggleoutput", outputid=protocol.UINT)
def toggleoutput(context, outputid):
    """
    *musicpd.org, audio output section:*

        ``toggleoutput {ID}``

        Turns an output on or off, depending on the current state.
    """
    if outputid == 0:
        mute_status = context.core.mixer.get_mute().get()
        success = context.core.mixer.set_mute(not mute_status)
        if not success:
            raise exceptions.MpdSystemError("problems toggling output")
    else:
        raise exceptions.MpdNoExistError("No such audio output")


@protocol.commands.add("outputs")
def outputs(context):
    """
    *musicpd.org, audio output section:*

        ``outputs``

        Shows information about all outputs.
    """
    muted = 1 if context.core.mixer.get_mute().get() else 0
    return [
        ("outputid", 0),
        ("outputname", "Mute"),
        ("outputenabled", muted),
    ]


@protocol.commands.add("outputset", outputid=protocol.UINT)
def outputset(context, outputid, name, value):
    """
    *musicpd.org, audio output section:*

        ``outputset {ID} {NAME} {VALUE}``

        Set a runtime attribute. These are specific to the output plugin, and
        supported values are usually printed in the ``outputs`` response.
    """
    if outputid == 0:
        # We don't use this part of MPD, treat everything read-only.
        raise exceptions.MpdNotImplemented
    else:
        raise exceptions.MpdNoExistError("No such audio output")
