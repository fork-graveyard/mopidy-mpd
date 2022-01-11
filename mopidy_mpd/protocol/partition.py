from mopidy_mpd import exceptions, protocol


@protocol.commands.add("partition", list_command=False)
def partition(context, name):
    """
    *musicpd.org, partition section:*

        ``partition {NAME}``

        Switch the client to a different partition.

    """
    raise exceptions.MpdNotImplemented  # TODO


@protocol.commands.add("listpartitions", list_command=False)
def listpartitions(context):
    """
    *musicpd.org, partition section:*

        ``listpartitions``

        Print a list of partitions. Each partition starts with a ``partition``
        keyword and the partition’s name, followed by information about the
        partition.


    """
    raise exceptions.MpdNotImplemented  # TODO


@protocol.commands.add("newpartition", list_command=False)
def newpartition(context, name):
    """
    *musicpd.org, partition section:*

        ``newpartition {NAME}``

        Create a new partition.

    """
    raise exceptions.MpdNotImplemented  # TODO


@protocol.commands.add("delpartition", list_command=False)
def delpartition(context, name):
    """
    *musicpd.org, partition section:*

        ``delpartition {NAME}``

        Delete a partition. The partition must be empty (no connected clients
        and no outputs).

    """
    raise exceptions.MpdNotImplemented  # TODO
