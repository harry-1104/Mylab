Manage pods, containers and images

Usage:
  podman [options] [command]

Available Commands:
  attach      Attach to a running container
  auto-update Auto update containers according to their auto-update policy
  build       Build an image using instructions from Containerfiles
  commit      Create new image based on the changed container
  container   Manage containers
  cp          Copy files/folders between a container and the local filesystem
  create      Create but do not start a container
  diff        Display the changes to the object's file system
  events      Show podman events
  exec        Run a process in a running container
  export      Export container's filesystem contents as a tar archive
  generate    Generate structured data based on containers, pods or volumes
  healthcheck Manage health checks on containers
  help        Help about any command
  history     Show history of a specified image
  image       Manage images
  images      List images in local storage
  import      Import a tarball to create a filesystem image
  info        Display podman system information
  init        Initialize one or more containers
  inspect     Display the configuration of object denoted by ID
  kill        Kill one or more running containers with a specific signal
  load        Load image(s) from a tar archive
  login       Login to a container registry
  logout      Logout of a container registry
  logs        Fetch logs for pod with one or more containers
  logs        Fetch the logs of one or more containers
  machine     Manage a virtual machine
  manifest    Manipulate manifest lists and image indexes
  mount       Mount a working container's root filesystem
  network     Manage networks
  pause       Pause all the processes in one or more containers
  play        Play containers, pods or volumes from a structured file
  pod         Manage pods
  port        List port mappings or a specific mapping for the container
  ps          List containers
  pull        Pull an image from a registry
  push        Push an image to a specified destination
  rename      Rename an existing container
  restart     Restart one or more containers
  rm          Remove one or more containers
  rmi         Removes one or more images from local storage
  run         Run a command in a new container
  save        Save image(s) to an archive
  search      Search registry for image
  secret      Manage secrets
  start       Start one or more containers
  stats       Display a live stream of container resource usage statistics
  stop        Stop one or more containers
  system      Manage podman
  tag         Add an additional name to a local image
  top         Display the running processes of a container
  unmount     Unmounts working container's root filesystem
  unpause     Unpause the processes in one or more containers
  unshare     Run a command in a modified user namespace
  untag       Remove a name from a local image
  version     Display the Podman version information
  volume      Manage volumes
  wait        Block on one or more containers

Options:
      --cgroup-manager string      Cgroup manager to use ("cgroupfs"|"systemd") (default "cgroupfs")
      --cni-config-dir string      Path of the configuration directory for CNI networks
      --conmon string              Path of the conmon binary
  -c, --connection string          Connection to use for remote Podman service
      --events-backend string      Events backend to use ("file"|"journald"|"none") (default "file")
      --help                       Help for podman
      --hooks-dir strings          Set the OCI hooks directory path (may be set multiple times) (default [/usr/share/containers/oci/hooks.d])
      --identity string            path to SSH identity file, (CONTAINER_SSHKEY)
      --log-level string           Log messages above specified level (trace, debug, info, warn, warning, error, fatal, panic) (default "warn")
      --namespace string           Set the libpod namespace, used to create separate views of the containers and pods on the system
      --network-cmd-path string    Path to the command for configuring the network
  -r, --remote                     Access remote Podman service (default false)
      --root string                Path to the root directory in which data, including images, is stored
      --runroot string             Path to the 'run directory' where all state information is stored
      --runtime string             Path to the OCI-compatible binary used to run containers, default is /usr/bin/runc
      --runtime-flag stringArray   add global flags for the container runtime
      --storage-driver string      Select which storage driver is used to manage storage of images and containers (default is overlay)
      --storage-opt stringArray    Used to pass an option to the storage driver
      --syslog                     Output logging information to syslog as well as the console (default false)
      --tmpdir string              Path to the tmp directory for libpod state content.
                                   
                                   Note: use the environment variable 'TMPDIR' to change the temporary storage location for container images, '/var/tmp'.
                                   
      --url string                 URL to access Podman service (CONTAINER_HOST) (default "unix:/run/user/0/podman/podman.sock")
  -v, --version                    version for podman
